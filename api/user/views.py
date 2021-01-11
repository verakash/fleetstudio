import random
import re
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import get_user_model , login , logout
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerUser
from rest_framework.decorators import authentication_classes, permission_classes, api_view, renderer_classes
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.parsers import JSONParser





# Create your views here.
# created session token to check if user is logged in
def generate_session_token(length= 10):
    tokens = ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(10))
    return tokens




# code for user login
@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse ({'error': 'send a post request with valid parameters'})

    username= request.POST['email']
    password= request.POST['password']


    if not re.match("[\w\.\+\-]+@[\w]+\.[a-z]{2,4}$", username):
        return JsonResponse({'error': "Enter a valid email"})

    if len(password) > 7:
        return JsonResponse({'error': 'Password should be less than 6'})

    UserModel = get_user_model()

    try:
        user= UserModel.objects.get(email= username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email= username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':"Previous session exists"})
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({"error": "Invalid Email"})

# code for user signout
def signout(request, id):

    logout(request)

    UserModel = get_user_model()

    try:
        user= UserModel.objects.get(pk = id)
        user.session_token = '0'
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({"error": "Invalid user ID"})

    return JsonResponse({'success': "logout success"})

# code for viewing user profile
def view_profile(request, id):
    UserModel = get_user_model()
    try:
        user= UserModel.objects.get(pk = id)

        usr_dict = UserModel.objects.filter(pk= id).values().first()
        usr_dict.pop('password')

        if user.session_token == 0:
            return JsonResponse({"error": "please login to view your profile"})
        else:
            return JsonResponse({'user': usr_dict})

    except UserModel.DoesNotExist:
        return JsonResponse({"error": "Invalid user ID"})





class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CustomerUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

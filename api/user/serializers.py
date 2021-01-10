from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes
from .models import CustomerUser
from django.contrib.auth import get_user_model
from django.http import JsonResponse
UserModel= get_user_model()
import re
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from .models import CustomerUser


class UserSerializer(serializers.HyperlinkedModelSerializer):



    def create(self, validated_data):
        instance= self.Meta.model(**validated_data)
        username = validated_data['email']
        phone= validated_data['phone']

        if not re.match("[\w\.\+\-]+@[\w]+\.[a-z]{2,4}$", username):
            raise serializers.ValidationError({"error": "Enter a valid email"})
        else:
            if not re.match("\w{3}-\w{3}-\w{4}", phone):
                raise serializers.ValidationError({"error": "Enter a valid phone"})

            else:
                password= validated_data.pop('password', None)
                if password is not None:
                    if len(password) >7:
                        raise serializers.ValidationError({"error": "Password length should not be greater than 6"})
                    instance.set_password(password)
                instance.save()
                return instance
    class Meta:
        model= CustomerUser
        extra_kwargs= {'password':{'write_only': True}}
        fields= ('name', 'email', 'phone', 'password'
        , 'is_active','is_staff', 'is_superuser')

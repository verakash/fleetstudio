from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class CustomerUser(AbstractUser):
    name= models.CharField(max_length=8 , default="Anonymous")
    email=  models.CharField(max_length=20 ,unique= True)

    username= None

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    # here max_length is 12 because of 2 hyphen to be added in the phone (ex. 991-900-4311)
    phone = models.CharField(max_length=12 ,blank= True, null= True)
    session_token= models.CharField(max_length=10 ,default=0)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created= False, **kwargs):
    if created:
        Token.objects.create(user=instance)

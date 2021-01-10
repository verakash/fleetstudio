from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class CustomerUser(AbstractUser):
    name= models.CharField(max_length=50 , default="Anonymous")
    email=  models.CharField(max_length=250 ,unique= True)

    username= None

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    phone = models.CharField(max_length=20 ,blank= True, null= True)
    gender = models.CharField(max_length=10 ,blank= True, null= True)

    session_token= models.CharField(max_length=10 ,default=0)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

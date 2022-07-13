from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=8)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BaseUserManager()
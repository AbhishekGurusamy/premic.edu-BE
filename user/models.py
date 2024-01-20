from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    image_url = models.CharField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

# class LoginDetails(models.Model):
#     userID = models.CharField(max_length=100)
#     logTime = models.DateTimeField(auto_now=True)
#     image_url = models.JSONField()


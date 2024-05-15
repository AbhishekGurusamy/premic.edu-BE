from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Deviceinfo(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    deviceid = models.CharField(max_length=250)


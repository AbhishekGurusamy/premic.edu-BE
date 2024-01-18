from django.contrib import admin
from django.urls import path
from .views import Registerview, Loginview, WhoAmI

urlpatterns = [
    path('register',Registerview.as_view()),
    path('login',Loginview.as_view()),
    path('whoami',WhoAmI.as_view())
]
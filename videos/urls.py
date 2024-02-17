from django.urls import path
from .views import Videoview

urlpatterns = [
    path('',Videoview.as_view())
]
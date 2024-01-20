from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Userserializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

# Create your views here.
class Registerview(APIView):

    def post(self,request):
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'details':serializer.data})

class Loginview(APIView):

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        image_url = request.data['image_url']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not available')
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')

        payload = {
            'id':user.id,
            'iat':datetime.datetime.utcnow(),
            'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=20)
        }

        token = jwt.encode(payload,'secret',algorithm='HS256')
        # serializers = Userserializer(user)
        return Response({'token':token})

class WhoAmI(APIView):

    def get(self,request):
        token = request.data['token']

        if not token:
            raise AuthenticationFailed('Not Authorized')
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Session Expired')

        user = User.objects.filter(id=payload['id'])
        serializer = Userserializer(user,many=True)
        return Response({'details':serializer.data})

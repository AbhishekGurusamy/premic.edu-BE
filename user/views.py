from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Userserializer
from .models import User, Deviceinfo
from django.contrib.auth.models import Group
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

# Create your views here.
class Registerview(APIView):

    def post(self,request):
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        group = Group.objects.get(name='Normal User')
        user.groups.add(group)
        user.save()
        return Response({'details':serializer.data})

class Loginview(APIView):

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        sys_id = request.data['device_id']

        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')

        payload = {
            'id':user.id,
            'iat':datetime.datetime.utcnow(),
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        }

        user_device = Deviceinfo.objects.filter(deviceid=sys_id)
        if len(user_device) == 0:
            Deviceinfo.objects.create(user_id_id=user.id, deviceid=sys_id)
        else:
            pass

        token = jwt.encode(payload,'secret',algorithm='HS256')
        role = user.groups.get(user=user.id).name
        response = {}
        response['username'] = user.username
        response['role'] = role
        response['token'] = token
        return Response({"details":response})

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

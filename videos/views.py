from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import VideSerializer
from .models import VideoDetails

# Create your views here.
class Videoview(APIView):

    def post(self, request):
        ser = VideSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'details':ser.data})

    def get(self, request):
        video = VideoDetails.objects.get(pk=request.data['id'])
        ser = VideSerializer(video)
        return Response({'result':ser.data})
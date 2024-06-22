from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import VideSerializer
from .models import VideoDetails

# Create your views here.
class Videoview(APIView):
    def post(self, request):
        # todo need check mp4 formate or not
        ser = VideSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'details':ser.data})

    def get(self, request):
        # video = VideoDetails.objects.get(pk=request.GET.get('id'))
        video = VideoDetails.objects.all().order_by('-id')
        ser = VideSerializer(video, many=True)
        return Response({'result':ser.data})

    def delete(self,request):
        videoId = request.GET.get('id')
        try:
            delete_obj = VideoDetails.objects.get(id=videoId)
            delete_obj.delete()
            return Response('Deleted')
        except:
            return Response('Video Not found')
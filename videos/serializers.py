from rest_framework import serializers
from .models import VideoDetails

class VideSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoDetails
        fields = ['id', 'title','description','videoFile']
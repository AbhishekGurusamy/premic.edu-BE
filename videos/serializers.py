from rest_framework import serializers
from .models import VideoDetails

class VideSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    videoFile = serializers.FileField()
    # timestamp   = serializers.DateTimeField()

    class Meta:
        model = VideoDetails
        fields = ['id', 'title','description','videoFile']
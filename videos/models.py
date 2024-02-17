from django.db import models

# Create your models here.
class VideoDetails(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(null=True)
    videoFile = models.FileField(null=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    # courseID = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
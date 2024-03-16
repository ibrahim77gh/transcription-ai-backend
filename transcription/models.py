from django.db import models
from django.conf import settings

# Create your models here.
class Transcription(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
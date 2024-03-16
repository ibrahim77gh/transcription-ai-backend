from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.
class TranscriptionView(ModelViewSet):
    serializer_class = TranscriptionSerializer
    def get_queryset(self):
        return Transcription.objects.filter(user = self.request.user).all()
    
    # def create(self, request, *args, **kwargs):
    #     pass
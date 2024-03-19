from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('transcription', TranscriptionView, basename='transcriptions')
urlpatterns=[]
urlpatterns+=router.urls
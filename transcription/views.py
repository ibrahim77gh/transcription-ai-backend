from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import os
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# import torch
# import librosa
# from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import whisper
import tempfile
# processor = AutoProcessor.from_pretrained("ihanif/whisper-medium-urdu")
# model = AutoModelForSpeechSeq2Seq.from_pretrained("ihanif/whisper-medium-urdu")

class TranscriptionView(ModelViewSet):
    serializer_class = TranscriptionSerializer

    def get_queryset(self):
        # transcriptions = Transcription.objects.filter(user = self.request.user).all()
        transcriptions = Transcription.objects.all()
        return transcriptions

    def create(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        
        if audio_file is None:
            return Response({'error': 'No audio file provided'}, status=400)
        
        # Save the audio file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
            for chunk in audio_file.chunks():
                temp_audio_file.write(chunk)
            temp_audio_file.close()
            # Load the temporary audio file
            temp_audio_path = temp_audio_file.name
            
            # Now proceed with transcribing
            model = whisper.load_model("medium")
            result = model.transcribe(audio=temp_audio_path, verbose=True, language='urdu')
            
            # Clean up temporary file
            os.unlink(temp_audio_path)
            
            print(result["text"])
            return Response(data={'text':result["text"]}, status=201)

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import os
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import torch
import librosa
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import whisper
processor = AutoProcessor.from_pretrained("ihanif/whisper-medium-urdu")
model = AutoModelForSpeechSeq2Seq.from_pretrained("ihanif/whisper-medium-urdu")

class TranscriptionView(ModelViewSet):
    serializer_class = TranscriptionSerializer

    def get_queryset(self):
        transcriptions = Transcription.objects.filter(user = self.request.user).all()
        return transcriptions

    def create(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        
        if audio_file is None:
            return Response({'error': 'No audio file provided'}, status=400)


        # Save the audio file temporarily


        model = whisper.load_model("medium")
        waveform, sampling_rate = librosa.load(audio_file, sr=16000)

        result = model.transcribe(waveform, language="urdu", fp16=False, verbose=True)
        print(result["text"])
        # with open('temp_audio.wav', 'wb') as temp_audio:
        #     for chunk in audio_file.chunks():
        #         temp_audio.write(chunk)

        # # Load the audio waveform and sampling rate using librosa
        # waveform, sampling_rate = librosa.load('temp_audio.wav', sr=16000)

        # # Ensure the waveform tensor has the correct shape and dimensions
        # if waveform.ndim > 1:
        #     waveform = waveform.mean(axis=0)

        # # Ensure the waveform tensor has the correct dtype and is on CPU
        # waveform = torch.tensor(waveform, dtype=torch.float32).cpu()

        # input_features = processor(
        #     waveform.numpy(), sampling_rate=sampling_rate, return_tensors="pt"
        # ).input_features
        # predicted_ids = model.generate(input_features)
        # transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

        # # Delete the temporary audio file
        # os.remove('temp_audio.wav')

        # # Assuming Transcription model has a field 'text' to store the transcription
        # transcription_text = transcription[0]

        # Save the transcription to your database
        # user = request.user
        # transcription_instance = Transcription.objects.create(text=transcription_text, user=user)

        # Serialize the transcription instance and return it in the response
        # serializer = TranscriptionSerializer(transcription_instance)
        return Response(data={'text':result["text"]}, status=201)

# # Create your views here.
# class TranscriptionView(ModelViewSet):
#     serializer_class = TranscriptionSerializer
#     def get_queryset(self):
#         transcriptions = Transcription.objects.all()
#         print(transcriptions)
#         return transcriptions

#         # return Transcription.objects.filter(user = self.request.user).all()
    
#     def create(self, request, *args, **kwargs):
#         pass
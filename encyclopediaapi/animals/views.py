from rest_framework import generics
from django.shortcuts import get_object_or_404
from animals import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics, status

class AnimalList(generics.ListCreateAPIView):
    
    queryset = models.Animals.objects.all()
    serializer_class = serializers.PartialAnimalSerializer


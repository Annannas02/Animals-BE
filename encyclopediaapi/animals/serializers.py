from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from animals import models

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animals
        fields = '__all__'

class PartialAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animals
        fields = ['id', 'name', 'species', 'location', 'diet']

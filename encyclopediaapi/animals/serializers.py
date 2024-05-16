from rest_framework import serializers
from animals import models

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animals
        fields = '__all__'

class PartialAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animals
        fields = ['name', 'species']
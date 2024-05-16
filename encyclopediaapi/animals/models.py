from django.db import models

class Animals(models.Model):
    name=models.CharField(max_length=100)
    species=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    habitat=models.CharField(max_length=100)
    location=models.CharField(max_length=20)
    diet=models.CharField(max_length=20)

    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
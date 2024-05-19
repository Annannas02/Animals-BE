from rest_framework import generics
from django.shortcuts import get_object_or_404
from animals import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

authorization_header = openapi.Parameter(
    'Authorization', 
    openapi.IN_HEADER, 
    description="Bearer <token>", 
    type=openapi.TYPE_STRING,
    required=True
)

page_param = openapi.Parameter(
    'page', 
    openapi.IN_QUERY, 
    description="Page number", 
    type=openapi.TYPE_INTEGER,
    required=False
)

class AnimalList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Animals.objects.all()
    serializer_class = serializers.PartialAnimalSerializer

    @swagger_auto_schema(
            manual_parameters=[authorization_header, page_param],
            operation_description="Retrieve a list of animals")
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new animal")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AnimalDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = models.Animals.objects.all()
    serializer_class = serializers.AnimalSerializer  # Use full serializer for detail view

    @swagger_auto_schema(
            manual_parameters=[authorization_header],
            operation_description="Retrieve animal details")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
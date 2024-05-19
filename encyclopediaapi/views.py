# views.py
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from drf_yasg.utils import swagger_auto_schema
from django.core.exceptions import ValidationError
from drf_yasg import openapi
from django.core.paginator import Paginator


authorization_header = openapi.Parameter(
    'Authorization', 
    openapi.IN_HEADER, 
    description="Bearer <token>", 
    type=openapi.TYPE_STRING,
    required=True
)

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
    },
    required=['username', 'password']
), responses={200: openapi.Response('Successful Login', schema=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Refresh Token'),
        'access': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Access Token'),
    }
)), 401: 'Invalid Credentials'})
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
        'is_staff': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Staff', default=False),
    },
    required=['username', 'password']
), responses={201: 'User registered successfully', 400: 'Bad Request'})
@api_view(['POST'])
def register(request):

    
    username = request.data.get('username')
    password = request.data.get('password')
    is_staff = request.data.get('is_staff')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate_password(password)
    except ValidationError as e:
        return Response({'error': list(e)}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, is_staff=is_staff)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
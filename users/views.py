from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import UserSerializer
import jwt
import os
# Create your views here.
jwtKey = os.environ.get("JWT_KEY")

@api_view(['POST'])
def adduser(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            payload = serializer.data
            del payload['username']
            token = jwt.encode(payload, jwtKey)
            payload['token'] = token
            return Response(payload, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_400_BAD_REQUEST)
    payload = {
                'email': user.email,
                'first_name' : user.first_name,
                'last_name' : user.last_name 
            }
    jwt_token = jwt.encode(payload, jwtKey)
    
    return Response(jwt_token,
                    status=status.HTTP_200_OK)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from bson import ObjectId
import datetime
import jwt
import time
import os

from .models import Post    
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
def posts_list(request):
    token = request.META.get('HTTP_X_AUTH_TOKEN') 
    if token is None:
        return Response({"Error" : "Token not provided"}, status=status.HTTP_401_UNAUTHORIZED)
        
    user = jwt.decode(token, os.environ.get("JWT_KEY"))
    if user is None:
        return Response({"Error" : "Invalid Token"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        user_id = request.query_params.get('user_id')
        data = Post.objects.all()
        if user_id:
            data = data.filter(user_id=user_id)
        serializer = PostSerializer(data, context={'request': request}, many= True)
        

        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        data["liked"] = False
        
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def posts_detail(request, _id):
    try:
        post = Post.objects.get(pk=ObjectId(_id))
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = PostSerializer(post)

        return Response(serializer.data)

    elif request.method == 'PUT':
        
        data = request.data
        data["liked"] = False
        serializer = PostSerializer(post, data=data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
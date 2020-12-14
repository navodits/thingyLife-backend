from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from bson import ObjectId
from .custom_storage import MediaStorage
from .serializers import PhotoSerializer
from .models import Image
import datetime
import jwt
import os


@api_view(['GET', 'POST'])
def upload_photo(request):
    if request.method == 'GET':
        user_id = request.query_params.get('user_id')
        data = Image.objects.all()
        if user_id:
            data = data.filter(user_id=user_id)
        serializer = PhotoSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        data = {}
        data['user_id'] = request.data.get('user_id')
        file = request.FILES.get('image')

        # do your validation here e.g. file size/type check

        # organize a path for the file in bucket

        media_storage = MediaStorage()
        filename = "image" + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        media_storage.save(filename, file)
        imageUrl = media_storage.url(filename)
        data['imageUrl'] = imageUrl
        print(data)
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

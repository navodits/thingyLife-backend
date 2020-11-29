from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from bson import ObjectId
from .custom_storage import MediaStorage
import datetime
import jwt
import os
    

@api_view(['POST'])
def upload_photo(request):
    file_obj = request.FILES['image']
    

    # do your validation here e.g. file size/type check
    
    # organize a path for the file in bucket
    

    media_storage = MediaStorage()

    if not media_storage.exists("bhangra"): # avoid overwriting existing file
        media_storage.save("bhangra", file_obj)
        file_url = media_storage.url("bhangra")
        print(file_url)

        return Response({
            'message': 'OK',
            'fileUrl': file_url,
        })
    else:
        return Response({
            'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                filename=file_obj.name,
                file_directory="photos",
                bucket_name=media_storage.bucket_name
            ),
        }, status=400)
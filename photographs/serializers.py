from rest_framework import serializers
from photographs.models import Image


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("_id", "imageUrl", "user_id")

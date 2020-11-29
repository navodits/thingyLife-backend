from rest_framework import serializers
from photographs.models import Photograph

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photograph
        fields = ("_id", "photo", "user_id")
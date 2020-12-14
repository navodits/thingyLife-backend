from rest_framework import serializers
from thingsHappend.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("_id", "title", "content", "datePosted", "liked", "user_id")

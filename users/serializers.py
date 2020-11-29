from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from djongo import models

class UserSerializer(serializers.ModelSerializer):
    
    username = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )        
    password = serializers.CharField(min_length=5, write_only=True)

    first_name = serializers.CharField(min_length=3)

    last_name = serializers.CharField(min_length=2)

    def create(self, validated_data):
        user = User.objects.create_user( validated_data['username'], validated_data['email'],
             validated_data['password'], first_name = validated_data['first_name'], last_name= validated_data['last_name'])
        return user

    class Meta:
        model = User
        fields = (  'username', 'password', 'first_name', 'last_name', 'email')
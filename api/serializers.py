from dataclasses import field
from turtle import title
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'reminder']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {
            'password':
            {
                'write_only': True,
                'required': True
            }
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user = user)
        return user
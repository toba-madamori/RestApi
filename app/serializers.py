from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import BlogModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['name', 'title', 'body', 'email', 'date']
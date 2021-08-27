from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogModel

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogModel
        fields = ['name', 'title', 'body', 'email', 'date', 'author']


class UserSerializer(serializers.ModelSerializer):
    blogs_id = serializers.PrimaryKeyRelatedField(many=True, queryset= BlogModel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'blogs_id']
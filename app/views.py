import re
from django.shortcuts import render
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework import serializers, views, status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def blog_home(request):
    if request.method == 'GET':
        articles = BlogModel.objects.all()
        serializer = BlogSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET', 'PUT', 'DELETE'])
def blogpost(request, pk):
    try:
        snippet = BlogModel.objects.get(pk=pk)
    except BlogModel.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)                            
            

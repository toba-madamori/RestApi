import re
from django.shortcuts import render
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework import serializers, views
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def blog_home(request):
    if request.method == 'GET':
        articles = BlogModel.objects.all()
        serializer = BlogSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)    

@api_view(['GET', 'PUT', 'DELETE'])
def blogpost(request, pk):
    try:
        snippet = BlogModel.objects.get(pk=pk)
    except BlogModel.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = BlogSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status = 204)                            
            

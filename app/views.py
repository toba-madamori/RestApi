from django.http.response import Http404
from django.shortcuts import render
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
# Create your views here.


class BlogListView(generics.ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
                     
                

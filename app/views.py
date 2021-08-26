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


class BlogListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, *kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, *kwargs)
        



class BlogDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)                            
                

from django.http.response import Http404
from django.shortcuts import render
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class BlogListView(APIView):
    def get(self,request, format=None):
        articles = BlogModel.objects.all()
        serializer = BlogSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    




class BlogDetailView(APIView):
    def get_object(self, pk):
        try:
            return BlogModel.objects.get(pk=pk)
        except BlogModel.DoesNotExist:
            raise Http404

    def get(self,request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BlogSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BlogSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)                            
                

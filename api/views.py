from django.shortcuts import render
from rest_framework import generics

from .serializers import BlogPostSerializer
from .models import BlogPost

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    

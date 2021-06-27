from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

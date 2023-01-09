from django.shortcuts import render
from .models import Category, Car
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, CarSerializer
from rest_framework import permissions

class CategoryView(ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]


class CarView(ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [
        permissions.AllowAny
    ]
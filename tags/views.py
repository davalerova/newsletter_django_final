from django.shortcuts import render
from rest_framework import permissions
from .serializers import TagSerializer
from .models import Tag
# Create your views here.

from rest_framework.viewsets import ModelViewSet

class TagViewSet(ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import News, Images
from .serializers import ImageSerializer, NewsSerializer


# Create your views here.

class ImageViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from about.models import About
from about.serializers import AboutSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

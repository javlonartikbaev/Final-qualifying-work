from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('image', ImageViewSet, basename='image')
router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),

]

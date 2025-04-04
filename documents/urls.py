from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('year', StudyYearViewSet, basename='year-post')
router.register('category', CategoryViewSet, basename='category-post')
router.register('document', DocumentViewSet, basename='document-post')

urlpatterns = [
    path('', include(router.urls)),

]

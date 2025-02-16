from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('get/year', StudyYearViewSetGET, basename='year-get')
router.register('post/year', StudyYearViewSet, basename='year-post')
router.register('get/category', CategoryViewSetGET, basename='category-get')
router.register('post/category', CategoryViewSet, basename='category-post')
router.register('get/document', DocumentViewSet, basename='document-get')
router.register('post/document', DocumentViewPost, basename='document-post')

urlpatterns = [
    path('', include(router.urls)),
    path('get/documents', DocumentViewSetGET.as_view(), name='document_get'),

]

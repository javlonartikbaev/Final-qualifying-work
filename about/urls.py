from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet

router = DefaultRouter()
router.register('', AboutViewSet, basename='about')

urlpatterns = [
    path('', include(router.urls)),
]

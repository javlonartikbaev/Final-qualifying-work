from django.urls import path, include
from rest_framework import routers

from .views import TeacherViewSet, TeachersPositionViewSetGET

router = routers.DefaultRouter()
router.register('teachers', TeacherViewSet)
router.register('positions', TeachersPositionViewSetGET)
urlpatterns = [
    path('', include(router.urls)),

]

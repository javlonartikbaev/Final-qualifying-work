from django.urls import path, include
from rest_framework import routers

from .views import (CreateTeacher,
                    ListTeachers,
                    DetailTeacher,
                    UpdateTeacher,
                    DeleteTeacher,
                    TeachersPositionViewSetGET)

router = routers.DefaultRouter()

router.register('positions', TeachersPositionViewSetGET)
urlpatterns = [
    path('', include(router.urls)),
    path('post/teacher/', CreateTeacher.as_view(), name='post-teacher'),
    path('put/teacher/<uuid:pk>/', UpdateTeacher.as_view(), name='put-teacher'),
    path('list/teacher/', ListTeachers.as_view(), name='list-teacher'),
    path('detail/teacher/', DetailTeacher.as_view(), name='detail-teacher'),
    path('detail/teacher/<uuid:pk>/', DetailTeacher.as_view(), name='detail-teacher-admin'),
    path('delete/teacher/<uuid:pk>/', DeleteTeacher.as_view(), name='delete-teacher'),

]

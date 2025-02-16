from rest_framework.viewsets import ReadOnlyModelViewSet

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer


# Create your views here.

class TeacherViewSet(ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

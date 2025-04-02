from rest_framework.viewsets import ModelViewSet

from teachers.models import Teacher, PositionTeacher
from teachers.serializers import TeacherSerializer
from .serializers import PositionSerializer


# Create your views here.
class TeachersPositionViewSetGET(ModelViewSet):
    queryset = PositionTeacher.objects.all()
    serializer_class = PositionSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.utils.representation import serializer_repr
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from yaml import serialize

from teachers.models import Teacher, PositionTeacher
from teachers.serializers import TeacherSerializer
from .serializers import PositionSerializer
from .permissions import CustomPermission


# Create your views here.
class TeachersPositionViewSetGET(ModelViewSet):
    queryset = PositionTeacher.objects.all()
    serializer_class = PositionSerializer


class CreateTeacher(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk=None):
        return get_object_or_404(Teacher, pk=pk)

    def post(self, request):

        user = request.user
        if user.role == 'admin':
            serializer = TeacherSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        elif user.role == 'teacher':
            return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


class ListTeachers(APIView):
    def get(self, request):
        user = request.user
        if user.role == 'admin':
            users = Teacher.objects.all()
            serializer = TeacherSerializer(users, many=True).data
            return Response(serializer, status=status.HTTP_200_OK)
        elif user.role == 'teacher':
            data = {
                "message": "You don't have permission to see list of teachers.",
            }
            return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class DetailTeacher(APIView):
    def get(self, request, pk=None):
        user = request.user
        if user.role == 'admin':
            teacher = Teacher.objects.get(id=pk)
            serializer = TeacherSerializer(teacher).data
            return Response(serializer, status=status.HTTP_200_OK)
        elif user.role == 'teacher':
            teacher = Teacher.objects.get(id=request.user.id)
            serializer = TeacherSerializer(teacher, many=False).data
            return Response(serializer, status=status.HTTP_200_OK)


class UpdateTeacher(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, pk):
        user = request.user
        if user.role == 'admin':
            try:
                teacher = Teacher.objects.get(id=pk)
                serializer = TeacherSerializer(teacher, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            except Teacher.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif user.role == 'teacher':
            try:
                teacher = Teacher.objects.get(id=request.user.id)
                serializer = TeacherSerializer(teacher, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            except Teacher.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    def patch(self, request):
        pass


class DeleteTeacher(APIView):
    def delete(self, request, pk):
        user = request.user
        if user.role == 'admin':
            try:
                teacher = Teacher.objects.get(id=pk)
                teacher.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Teacher.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif user.role == 'teacher':
            message = "You don't have permission to delete teacher."
            return Response(message, status.HTTP_405_METHOD_NOT_ALLOWED)

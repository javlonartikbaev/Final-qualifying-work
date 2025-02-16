from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# Create your views here.

class StudyYearViewSetGET(viewsets.ModelViewSet):
    serializer_class = StudyYearSerializerGET
    allowed_methods = ['get', ]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.teacher
        year = Year.objects.filter(teacher_id=user)
        return year


class StudyYearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = StudyYearSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        teacher = self.request.user.teacher
        serializer.save(teacher_id=teacher)


class CategoryViewSetGET(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializerGET
    allowed_methods = ['get', ]

    def get_queryset(self):
        user = self.request.user.teacher
        category = Category.objects.filter(teacher_id=user)
        return category


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        teacher = self.request.user.teacher
        serializer.save(teacher_id=teacher)


class DocumentViewSetGET(APIView):
    def get(self, request):
        documents = Documents.objects.filter(visible=True)
        serializers = DocumentSerializerGET(documents, many=True, context={'request': request})
        data = {
            'documents': serializers.data,

        }
        return Response(status=status.HTTP_200_OK, data=data)


class DocumentViewSet(viewsets.ModelViewSet):
    """ только гет request.user = teacher_id """

    permission_classes = [IsAuthenticated]
    serializer_class = DocumentSerializer
    allowed_methods = ['get', ]

    def get_queryset(self):
        teacher = self.request.user.teacher
        document = Documents.objects.filter(teacher_id=teacher)
        return document


class DocumentViewPost(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializerPOST

    def perform_create(self, serializer):
        teacher = self.request.user.teacher
        serializer.save(teacher_id=teacher)

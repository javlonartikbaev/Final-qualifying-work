from xml.dom.minidom import Document

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# Create your views here.


class StudyYearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = StudyYearSerializer


# permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumtenSerializer

    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        teacher = self.request.user
        serializer.save(teacher_id=teacher)

    def get_queryset(self):
        queryset = Documents.objects.filter(teacher_id=self.request.user.id)
        if self.request.user.is_authenticated:
            queryset = Documents.objects.filter(teacher_id=self.request.user.id)
        elif self.request.user.is_anonymous:
            queryset = Documents.objects.filter(visible=True)
        return queryset

# class DocumentViewSetGET(APIView):
#     def get(self, request):
#         documents = Documents.objects.filter(visible=True)
#         serializers = DocumentSerializerGET(documents, many=True, context={'request': request})
#         data = {
#             'documents': serializers.data,
#
#         }
#         return Response(status=status.HTTP_200_OK, data=data)
#
#
# class DocumentViewSet(viewsets.ModelViewSet):
#     """ только гет request.user = teacher_id """
#
#     permission_classes = [IsAuthenticated]
#     serializer_class = DocumentSerializer
#     allowed_methods = ['get', ]
#
#     def get_queryset(self):
#         teacher = self.request.user.teacher
#         document = Documents.objects.filter(teacher_id=teacher)
#         return document
#
#
# class DocumentViewPost(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Documents.objects.all()
#     serializer_class = DocumentSerializerPOST
#
#     def perform_create(self, serializer):
#         teacher = self.request.user.teacher
#         serializer.save(teacher_id=teacher)

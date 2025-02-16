from rest_framework import serializers

from teachers.serializers import TeacherSerializer
from .models import *


class StudyYearSerializerGET(serializers.ModelSerializer):
    teacher_id = TeacherSerializer()

    class Meta:
        model = Year
        fields = '__all__'


class StudyYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['year', ]


class CategorySerializerGET(serializers.ModelSerializer):
    teacher_id = TeacherSerializer()

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', ]


class TeacherDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name']


class YearDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['year']


class CategoryDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class DocumentSerializerGET(serializers.ModelSerializer):
    """Get где visible = True"""
    teacher_id = TeacherDocumentSerializer()
    category_id = CategoryDocumentSerializer()
    document_year = YearDocumentSerializer()

    class Meta:
        model = Documents
        fields = ['document_name', 'document_description', 'document', 'teacher_id', 'document_year', 'category_id',
                  'visible']


class DocumentSerializer(serializers.ModelSerializer):
    """GET только request.user = teacher_id"""
    teacher_id = TeacherDocumentSerializer()
    category_id = CategoryDocumentSerializer()
    document_year = YearDocumentSerializer()

    class Meta:
        model = Documents
        fields = ['document_name', 'document_description', 'document', 'teacher_id', 'document_year', 'category_id',
                  'visible']


class DocumentSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ['document_name', 'document_description', 'document', 'document_year', 'category_id',
                  'visible']

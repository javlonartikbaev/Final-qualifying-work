from rest_framework import serializers

from teachers.serializers import TeacherSerializer
from .models import *
from .models import Documents


class StudyYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TeacherDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name']


class DocumtenSerializer(serializers.ModelSerializer):
    document_year = serializers.PrimaryKeyRelatedField(queryset=Year.objects.all())
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    teacher_id = TeacherSerializer(read_only=True)

    class Meta:
        model = Documents
        fields = '__all__'

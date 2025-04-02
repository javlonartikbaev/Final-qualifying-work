from rest_framework import serializers

from teachers.models import Teacher, PositionTeacher
from .managers import UserCustomManager


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionTeacher
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    position_id = serializers.PrimaryKeyRelatedField(queryset=PositionTeacher.objects.all())

    class Meta:
        model = Teacher
        exclude = ('last_login',)

    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)

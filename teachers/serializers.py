from django.contrib.auth.hashers import make_password
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

    def update(self, instance, validated_data):
        position_id = validated_data.pop('position_id', instance.position_id)
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.position_id = position_id
        instance.save()
        return instance

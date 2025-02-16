from rest_framework import serializers

from teachers.models import Teacher


class PositionSerializer(serializers.Serializer):
    position_name = serializers.CharField()
    number_of_position = serializers.IntegerField()


class TeacherSerializer(serializers.ModelSerializer):
    position_id = PositionSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'phone_number', 'position_id']

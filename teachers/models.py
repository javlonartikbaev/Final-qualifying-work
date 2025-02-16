from django.contrib.auth.models import User, AbstractUser
from django.db import models


class PositionTeacher(models.Model):
    position_name = models.CharField(max_length=60)
    number_of_position = models.IntegerField(default=1)

    class Meta:
        db_table = 'position_teacher'
        verbose_name = 'Должности'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.position_name


# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    logo_teacher = models.ImageField(upload_to='teachers/')
    position_id = models.ForeignKey(PositionTeacher, on_delete=models.CASCADE, related_name='position_teacher')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

    class Meta:
        db_table = 'teacher'
        verbose_name = 'Учителя'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.full_name

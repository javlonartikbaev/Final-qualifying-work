import uuid

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from teachers.managers import UserCustomManager


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
class Teacher(AbstractBaseUser):
    class ROLE(models.TextChoices):
        ADMIN = 'admin',
        TEACHER = 'teacher',

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True)
    logo_teacher = models.ImageField(upload_to='teachers/', null=True, blank=True)
    position_id = models.ForeignKey(PositionTeacher, on_delete=models.CASCADE, related_name='position_teacher')
    role = models.CharField(max_length=10, choices=ROLE.choices, default=ROLE.TEACHER)

    objects = UserCustomManager()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'teacher'
        verbose_name = 'Учителя'

        verbose_name_plural = verbose_name

    def __str__(self):
        return self.full_name

import os

from django.db import models
from rest_framework.exceptions import ValidationError

from teachers.models import Teacher


# Create your models here.

class Year(models.Model):
    year = models.CharField(max_length=9)

    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'year'
        verbose_name = 'Учебные годы'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.year


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_category')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


class Documents(models.Model):
    document_name = models.CharField(max_length=254)
    document_description = models.TextField(null=True, blank=True)
    document = models.FileField(upload_to='documents')
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_document')
    document_year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='document_year')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_document')
    visible = models.BooleanField(default=False)

    class Meta:
        db_table = 'documents'
        verbose_name = 'Документы'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.document_name

    def clean(self):
        super().clean()
        allowed_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx']
        ext = os.path.splitext(self.document.name)[1]
        if ext.lower() not in allowed_extensions:
            raise ValidationError(
                f'Файлы с расширением {ext} не поддерживаются. Допустимые форматы: {", ".join(allowed_extensions)}')

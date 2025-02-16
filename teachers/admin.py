from django.contrib import admin

from .models import *

@admin.register(PositionTeacher)
class PositionTeacherAdmin(admin.ModelAdmin):
    list_display = ('id','position_name','number_of_position')
# Register your models here.
@admin.register(Teacher)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position_id')
    search_fields = ('full_name',)

from django.contrib import admin
from .models import WorkDetail

# Register your models here.


@admin.register(WorkDetail)
class WorkDetailAdmin(admin.ModelAdmin):
    list_display = ('project', "project_type", 'duration', "is_complete")
    list_filter = ('is_complete', )

from django.contrib import admin
from .models import WorkDetail

# Register your models here.
@admin.register(WorkDetail)
class WorkDetailAdmin(admin.ModelAdmin):
	pass
from atexit import register

from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)
# @register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'completed')
#     list_filter = ('completed',)
#     search_fields = ('title',)

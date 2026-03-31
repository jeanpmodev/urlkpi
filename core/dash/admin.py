from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "task_content", "pub_date","done"]

admin.site.register(Task, TaskAdmin)
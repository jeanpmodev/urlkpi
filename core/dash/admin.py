from django.contrib import admin
from .models import Task, Boiler, Service


class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "task_content", "pub_date", "done"]


class BoilerAdmin(admin.ModelAdmin):
    list_display = ["id", "boiler_type", "boiler_code"]
    search_fields = ['boiler_code']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "service_name", "service_status"]


admin.site.register(Task, TaskAdmin)
admin.site.register(Boiler, BoilerAdmin)
admin.site.register(Service, ServiceAdmin)

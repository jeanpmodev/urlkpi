from django.contrib import admin
from .models import Task, Boiler, Service, ErrorManagement, Navbar


@admin.action(description="the selected tasks as completed.")
def task_is_done(modeladmin, request, queryset):
    queryset.update(done=True)


class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "task_content", "pub_date", "done"]
    ordering = ["id"]
    actions = [task_is_done]


class BoilerAdmin(admin.ModelAdmin):
    list_display = ["id", "boiler_type", "boiler_code"]
    search_fields = ['boiler_code']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "service_name", "service_status"]


class ErrorManagementAdmin(admin.ModelAdmin):
    list_display = ["id", "error_type", "error_amount", "error_datetime"]
    search_fields = ['error_datetime']


class NavbarAdmin(admin.ModelAdmin):
    list_display = ["id", "btn_name", "slug", "icon"]
    prepopulated_fields = {"slug": ("btn_name",)}


admin.site.register(Task, TaskAdmin)
admin.site.register(Boiler, BoilerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ErrorManagement, ErrorManagementAdmin)
admin.site.register(Navbar, NavbarAdmin)

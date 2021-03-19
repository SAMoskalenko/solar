from django.contrib import admin

from .models import Sites


@admin.register(Sites)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'is_active', 'last_check']
    ordering = ['id']
    search_fields = ['name', 'url', 'is_active', 'last_check']

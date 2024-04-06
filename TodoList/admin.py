from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created_at']
    list_filter = ['completed']
    search_fields = ['title', 'description']
    list_editable = ['completed']
    list_display_links = ['title']




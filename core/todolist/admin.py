from django.contrib import admin
from .models import ToDoItem


@admin.register(ToDoItem)
class ToDoAdmin(admin.ModelAdmin):
    fields = ["author", "description", "completed"]

from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = (
        'name',
        'color'
    )
    search_fields = (
        'name',
    )



@admin.register(Task)
class Task(admin.ModelAdmin):
    pass
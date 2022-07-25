from django.contrib import admin
from .models import *
from rest_framework.authtoken.admin import TokenAdmin


# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Description', 'Date', 'Completed']


TokenAdmin.raw_id_fields = ['user']

from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models
from .models import Manager


class UserAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'login', 'deleted']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Manager, UserAdmin)
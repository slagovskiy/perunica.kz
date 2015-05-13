from django.contrib import admin
from .models import Global


class GlobalAdmin(admin.ModelAdmin):
    ordering = ['active']
    list_display = ['active', 'meta_title']

admin.site.register(Global, GlobalAdmin)
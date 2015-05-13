from django.contrib import admin
from .models import Global


class GlobalAdmin(admin.ModelAdmin):
    ordering = ['active']
    list_display = ['meta_title', 'active']

admin.site.register(Global, GlobalAdmin)
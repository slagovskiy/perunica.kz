from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'link', 'admin_image_list', 'deleted']
    readonly_fields = ['admin_image']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Banner, BannerAdmin)
from django.contrib import admin
from .models import Global, Image, SU


class GlobalAdmin(admin.ModelAdmin):
    ordering = ['active']
    list_display = ['active', 'meta_title']


class SUAdmin(admin.ModelAdmin):
    ordering = ['active']
    list_display = ['active', 'name']


class ImageAdmin(admin.ModelAdmin):
    ordering = ['name']
    readonly_fields = ['code', 'admin_image']
    list_display = ['name', 'admin_image_list', 'code']


admin.site.register(Global, GlobalAdmin)
admin.site.register(SU, SUAdmin)
admin.site.register(Image, ImageAdmin)
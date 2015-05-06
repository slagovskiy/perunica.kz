from django.contrib import admin
from .models import Menu, SubMenu


class MenuAdmin(admin.ModelAdmin):
    ordering = ['sort', 'name']
    list_display = ['slug', 'name', 'sort', 'deleted']
    list_filter = ['slug']
    search_fields = ['slug']


class SubMenuAdmin(admin.ModelAdmin):
    ordering = ['menu', 'name']
    list_display = ['slug', 'menu', 'name', 'deleted']
    list_filter = ['slug']
    search_fields = ['slug']


admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
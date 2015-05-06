from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    #fields = ['sort', 'slug', 'name', 'deleted']
    ordering = ['sort', 'name']
    list_display = ['slug', 'name', 'sort', 'deleted']
    list_filter = ['slug']
    search_fields = ['slug']


admin.site.register(Menu, MenuAdmin)
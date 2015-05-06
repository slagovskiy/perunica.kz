from django.contrib import admin
from .models import Menu, SubMenu, Unit, Goods


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


class UnitAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'deleted']
    list_filter = ['name']
    search_fields = ['name']


class GoodsAdmin(admin.ModelAdmin):
    ordering = ['menu', 'is_sticked', 'is_new', 'name']
    list_display = ['name', 'menu', 'price', 'is_sticked', 'is_new', 'is_on_first', 'deleted']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Goods, GoodsAdmin)
from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models
from .models import Menu, SubMenu, Unit, Goods, GoodsGroup, GoodsLinkGroup, Order, OrderBody, OrderHistory


class MenuAdmin(admin.ModelAdmin):
    ordering = ['sort', 'name']
    list_display = ['slug', 'name', 'sort', 'admin_image_list', 'deleted']
    readonly_fields = ['admin_image']
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
    list_display = ['name', 'menu', 'price', 'admin_image_list', 'is_sticked', 'is_new', 'is_on_first', 'deleted']
    readonly_fields = ['admin_image']
    list_filter = ['name']
    search_fields = ['name']


class GoodsLinkInLine(admin.StackedInline):
    model = GoodsLinkGroup
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': SelectMultiple(attrs={'size':'14'})
        },
        }


class GoodsGroupAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'deleted']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [
        GoodsLinkInLine,
    ]


class OrderBodyInLine(admin.StackedInline):
    model = OrderBody


class OrderHistoryLine(admin.StackedInline):
    model = OrderHistory

class OrderAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ['number', 'status', 'summ', 'added', 'fio', 'phone', 'sended']
    inlines = [
        OrderBodyInLine,
        OrderHistoryLine
    ]


admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsGroup, GoodsGroupAdmin)
admin.site.register(Order, OrderAdmin)
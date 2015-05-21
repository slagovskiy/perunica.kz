from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    ordering = ['date', 'title']
    list_display = ['date', 'title', 'deleted']


admin.site.register(News, NewsAdmin)

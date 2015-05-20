from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    ordering = ['date', 'name']
    list_display = ['date', 'name', 'allowed', 'deleted']


admin.site.register(Feedback, FeedbackAdmin)

from django.db import models
import uuid
import os


class Feedback(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'Date')
    title = models.CharField(max_length=255, default=u'', verbose_name=u'Title')
    message = models.TextField(default=u'', null=True, blank=True, verbose_name=u'Message')

    def __str__(self):
        return self.title

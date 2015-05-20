from django.db import models
import uuid
import os


class Feedback(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    allowed = models.BooleanField(default=False, verbose_name=u'Allowed')
    date = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name=u'Date')
    name = models.CharField(max_length=255, default=u'', verbose_name=u'Name')
    email = models.EmailField(max_length=255, default=u'', null=True, blank=True, verbose_name=u'Email')
    phone = models.EmailField(max_length=255, default=u'', null=True, blank=True, verbose_name=u'Phone')
    comment = models.EmailField(max_length=255, default=u'', null=True, blank=True, verbose_name=u'Comment')

    def __str__(self):
        return self.name

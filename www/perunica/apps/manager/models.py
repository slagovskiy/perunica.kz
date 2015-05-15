from django.contrib.auth.models import User
from django.db import models
import uuid
import os


class User(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    login = models.CharField(max_length=255, default=u'', verbose_name=u'Login', unique=True)
    password = models.CharField(max_length=255, default=u'', verbose_name=u'Password')
    name = models.CharField(max_length=255, default=u'', verbose_name=u'Name')
    email = models.EmailField(max_length=255, default=u'', null=True, blank=True, verbose_name=u'Email')

    def __str__(self):
        return '%s [%s]' % (self.name, self.login)

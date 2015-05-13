from django.db import models


class Global(models.Model):
    active = models.BooleanField(unique=True, default=True, verbose_name=u'Active')
    meta_title = models.CharField(max_length=255, default='', verbose_name=u'Meta title')
    meta_description = models.TextField(max_length=1024, default='', verbose_name=u'Meta description')
    meta_keywords = models.TextField(max_length=1024, default='', verbose_name=u'Meta keywords')
    order_min_sum = models.FloatField(default=300, verbose_name=u'Minimal order sum')

    def __str__(self):
        return self.meta_title
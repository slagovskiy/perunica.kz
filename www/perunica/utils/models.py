from django.db import models
import uuid
import os


class Global(models.Model):
    active = models.BooleanField(unique=True, default=True, verbose_name=u'Active')
    meta_title = models.CharField(max_length=255, default='', verbose_name=u'Meta title')
    meta_description = models.TextField(max_length=1024, default='', verbose_name=u'Meta description')
    meta_keywords = models.TextField(max_length=1024, default='', verbose_name=u'Meta keywords')
    order_min_sum = models.FloatField(default=300, verbose_name=u'Minimal order sum')

    def __str__(self):
        return self.meta_title


class Image(models.Model):
    name = models.CharField(max_length=256, default='', verbose_name=u'Image name')
    def upload_to(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(str(uuid.uuid1()), ext)
        return os.path.join('images', filename)
    image = models.ImageField(upload_to=upload_to, null=True, verbose_name=u'Image')

    def __str__(self):
        return self.name

    def code(self):
        return '<img src="' + self.image.url + '" />'

    def admin_image_list(self):
        if self.image:
            return '<img style="max-height: 32px;" src="' + self.image.url + '" />'
        else:
            return ''

    def admin_image(self):
        if self.image:
            return '<img src="' + self.image.url + '" />'
        else:
            return ''

    admin_image_list.allow_tags = True
    admin_image_list.short_description = u'Image'
    admin_image.allow_tags = True
    admin_image.short_description = u'Image'
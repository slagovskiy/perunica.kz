from django.db import models
import uuid
import os


class Banner(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name=u'Name')
    link = models.CharField(max_length=255, verbose_name=u'link')

    def upload_to(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(str(uuid.uuid1()), ext)
        return os.path.join('banner', filename)
    image = models.ImageField(upload_to=upload_to, null=True, verbose_name=u'Image')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/banner/' % self.id

    def admin_image_list(self):
        if self.image:
            return '<img style="width: 122px; height: 24px;" src="%s"/>' % self.image.url
        else:
            return ''

    def admin_image(self):
        if self.image:
            return '<img src="%s"/>' % self.image.url
        else:
            return ''

    admin_image_list.allow_tags = True
    admin_image_list.short_description = u'Image'
    admin_image.allow_tags = True
    admin_image.short_description = u'Image'

    class Meta:
        ordering = ['name']
        verbose_name = u'Banner'
        verbose_name_plural = u'Banner'
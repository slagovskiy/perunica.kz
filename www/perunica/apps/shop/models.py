from django.db import models

class Menu(models.Model):
    slug = models.SlugField(unique=True, max_length=255, verbose_name=u'Slug')
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.TextField(max_length=255, verbose_name=u'Name')
    sort = models.IntegerField(default=10, verbose_name=u'Sort')
    icon = models.ImageField(upload_to='menu_icons', null=True, verbose_name=u'Icon')

    def __str__(self):
        return '[%s] %s' % (self.sort, self.name)

    def get_absolute_url(self):
        return '/menu/%s/' % self.slug

    class Meta:
        ordering = ['sort', 'name']
        verbose_name = u'Menu'
        verbose_name_plural = u'Main menu'



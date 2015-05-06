from django.db import models


class Menu(models.Model):
    slug = models.SlugField(unique=True, max_length=255, verbose_name=u'Slug')
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name=u'Name')
    sort = models.IntegerField(default=10, verbose_name=u'Sort')
    icon = models.ImageField(upload_to='menu_icons', null=True, verbose_name=u'Icon')

    def __str__(self):
        return '[%s] %s' % (self.sort, self.name)

    def get_absolute_url(self):
        return '/shop/menu/%s/' % self.slug

    def admin_image_list(self):
        return '<img style="width: 24px; height: 24px;" src="%s"/>' % self.icon.url

    def admin_image(self):
        return '<img src="%s"/>' % self.icon.url

    admin_image_list.allow_tags = True
    admin_image_list.short_description = u'Icon'
    admin_image.allow_tags = True
    admin_image.short_description = u'Icon'

    class Meta:
        ordering = ['sort', 'name']
        verbose_name = u'Menu'
        verbose_name_plural = u'Main menu'


class SubMenu(models.Model):
    slug = models.SlugField(unique=True, max_length=255, verbose_name=u'Slug')
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name=u'Name')
    menu = models.ForeignKey(Menu)

    def __str__(self):
        return '[%s] %s' % (self.menu.name, self.name)

    def get_absolute_url(self):
        return '/shop/menu/%s/%s/' % (self.menu.slug, self.slug)

    class Meta:
        ordering = ['name']
        verbose_name = u'Sub menu'
        verbose_name_plural = u'Sub menu'


class Unit(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u'Unit'
        verbose_name_plural = u'Units'


class Goods(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name='Name')
    image = models.ImageField(upload_to='goods', null=True, verbose_name=u'Image')
    description = models.TextField(max_length=1024, verbose_name=u'Description')
    weight = models.IntegerField(default=0, verbose_name=u'Weight')
    unit = models.ForeignKey(Unit)
    price = models.FloatField(default=0, verbose_name=u'Price')
    menu = models.ForeignKey(Menu)
    sub_menu = models.ForeignKey(SubMenu, null=True, blank=True)
    is_new = models.BooleanField(default=False, verbose_name=u'New')
    is_sticked = models.BooleanField(default=False, verbose_name=u'Sticked on top')
    is_on_first = models.BooleanField(default=False, verbose_name=u'On first')

    def __str__(self):
        return '[%s] %s' % (self.menu.name, self.name)

    def get_absolute_url(self):
        return '/shop/item/%s/' % self.id

    def admin_image_list(self):
        return '<img style="width: 24px; height: 24px;" src="%s"/>' % self.image.url

    def admin_image(self):
        return '<img src="%s"/>' % self.image.url

    admin_image_list.allow_tags = True
    admin_image_list.short_description = u'Image'
    admin_image.allow_tags = True
    admin_image.short_description = u'Image'

    class Meta:
        ordering = ['menu', 'is_sticked', 'is_new', 'name']
        verbose_name = u'Goods'
        verbose_name_plural = u'Goods'

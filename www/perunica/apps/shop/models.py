from django.contrib.auth.models import User
from django.db import models
import uuid
import os


class Menu(models.Model):
    slug = models.SlugField(unique=True, max_length=255, verbose_name=u'Slug')
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name=u'Name')
    sort = models.IntegerField(default=10, verbose_name=u'Sort')

    def upload_to(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(str(uuid.uuid1()), ext)
        return os.path.join('menu_icons', filename)
    icon = models.ImageField(upload_to=upload_to, null=True, verbose_name=u'Icon')
    banner = models.ImageField(upload_to=upload_to, null=True, blank=True, verbose_name=u'Banner')

    def __str__(self):
        return '[%s] %s' % (self.sort, self.name)

    def get_absolute_url(self):
        return '/shop/menu/%s/' % self.slug

    def admin_image_list(self):
        if self.icon:
            return '<img style="width: 24px; height: 24px;" src="%s"/>' % self.icon.url
        else:
            return ''

    def admin_image(self):
        if self.icon:
            return '<img src="%s"/>' % self.icon.url
        else:
            return ''

    def admin_banner_list(self):
        if self.banner:
            return '<img style="width: 122px; height: 24px;" src="%s"/>' % self.banner.url
        else:
            return ''

    def admin_banner(self):
        if self.banner:
            return '<img src="%s"/>' % self.banner.url
        else:
            return ''

    admin_image_list.allow_tags = True
    admin_image_list.short_description = u'Icon'
    admin_image.allow_tags = True
    admin_image.short_description = u'Icon'
    admin_banner_list.allow_tags = True
    admin_banner_list.short_description = u'Banner'
    admin_banner.allow_tags = True
    admin_banner.short_description = u'Banner'

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


class GoodsGroup(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name=u'Name')
    title = models.CharField(max_length=255, default=u'', verbose_name=u'Title')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u'Goods group'
        verbose_name_plural = u'Goods groups'


class Goods(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(max_length=1024, verbose_name=u'Description')
    weight = models.IntegerField(default=0, verbose_name=u'Weight')
    unit = models.ForeignKey(Unit)
    price = models.FloatField(default=0, verbose_name=u'Price')
    menu = models.ForeignKey(Menu)
    sub_menu = models.ForeignKey(SubMenu, null=True, blank=True)
    is_new = models.BooleanField(default=False, verbose_name=u'New')
    is_sticked = models.BooleanField(default=False, verbose_name=u'Sticked on top')
    is_on_first = models.BooleanField(default=False, verbose_name=u'On first')
    choice = models.ForeignKey(GoodsGroup, null=True, blank=True, verbose_name=u'Choice')
    option1 = models.ForeignKey(GoodsGroup, null=True, related_name='o1', blank=True, verbose_name=u'Option 1')
    option2 = models.ForeignKey(GoodsGroup, null=True, related_name='o2', blank=True, verbose_name=u'Option 2')
    option3 = models.ForeignKey(GoodsGroup, null=True, related_name='o3', blank=True, verbose_name=u'Option 3')

    def upload_to(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(str(uuid.uuid1()), ext)
        return os.path.join('goods', filename)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True, verbose_name=u'Image')

    def __str__(self):
        return '[%s] %s' % (self.menu.name, self.name)

    def get_absolute_url(self):
        return '/shop/item/%s/' % self.id

    def admin_image_list(self):
        if self.image:
            return '<img style="width: 24px; height: 24px;" src="%s"/>' % self.image.url
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
        ordering = ['menu', 'is_sticked', 'is_new', 'name']
        verbose_name = u'Goods'
        verbose_name_plural = u'Goods'


class GoodsLinkGroup(models.Model):
    group = models.OneToOneField(GoodsGroup)
    goods = models.ManyToManyField(Goods)


class Order(models.Model):
    CASHE_PAYMENT = 1
    CARD_PAYMENT = 2

    PAYMENT_CHOICES = (
        (CASHE_PAYMENT, 'Наличные'),
        (CARD_PAYMENT, 'Карта'),
    )

    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    uuid = models.CharField(max_length=80, default=u'', verbose_name=u'UUID')
    fio = models.CharField(max_length=255, default=u'', verbose_name=u'Name')
    phone = models.CharField(max_length=255, default=u'', verbose_name=u'Phone')
    email = models.CharField(max_length=255, default=u'', verbose_name=u'Phone')
    address = models.CharField(max_length=255, default=u'', verbose_name=u'Address')
    payment = models.SmallIntegerField(verbose_name=u'Payment', choices=PAYMENT_CHOICES, default=CASHE_PAYMENT)
    date = models.DateTimeField(auto_now=True, verbose_name=u'Added')
    sended = models.BooleanField(default=False, verbose_name=u'Sended')

    def number(self):
        return '%06d' % self.id

    def status(self):
        return self.orderhistory_set.all().last()

    def added(self):
        return self.date.strftime('%Y/%m/%d %H:%M:%S')
        
    def payment_name(self):
        if self.payment == 1:
            return 'Наличные'
        elif self.payment == 2:
            return 'Карта'
        else:
            return self.payment

    def summ(self):
        s = 0
        for item in self.orderbody_set.all():
            s += item.price * item.count
            if item.option1:
                s += item.price_o1 * item.count_o1
            if item.option2:
                s += item.price_o2 * item.count_o2
            if item.option3:
                s += item.price_o3 * item.count_o3
        return s

    def get_manager_url(self):
        return '/manager/order/' + str(self.id) + '/'

class OrderBody(models.Model):
    deleted = models.BooleanField(default=False, verbose_name=u'Deleted')
    order = models.ForeignKey(Order)
    goods = models.ForeignKey(Goods)
    option1 = models.ForeignKey(Goods, blank=True, null=True, related_name='o1')
    option2 = models.ForeignKey(Goods, blank=True, null=True, related_name='o2')
    option3 = models.ForeignKey(Goods, blank=True, null=True, related_name='o3')
    price = models.FloatField(default=0, verbose_name=u'Price')
    price_o1 = models.FloatField(default=0, verbose_name=u'Price option 1')
    price_o2 = models.FloatField(default=0, verbose_name=u'Price option 2')
    price_o3 = models.FloatField(default=0, verbose_name=u'Price option 3')
    count = models.FloatField(default=0, verbose_name=u'Count')
    count_o1 = models.FloatField(default=0, verbose_name=u'Count option 1')
    count_o2 = models.FloatField(default=0, verbose_name=u'Count option 2')
    count_o3 = models.FloatField(default=0, verbose_name=u'Count option 3')
    change = models.DateTimeField(auto_now=True, verbose_name=u'Last change')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name=u'User')


class OrderHistory(models.Model):
    CANCEL_STATUS = 0
    NEW_STATUS = 1
    WORK_STATUS = 2
    SEND_STATUS = 3
    DONE_STATUS = 4

    STATUS_CHOICES = (
        (CANCEL_STATUS, 'Отменен'),
        (NEW_STATUS, 'Новый'),
        (WORK_STATUS, 'Готовится'),
        (SEND_STATUS, 'Доставляется'),
        (DONE_STATUS, 'Выдан'),
    )

    order = models.ForeignKey(Order)
    status = models.SmallIntegerField(verbose_name=u'Status', choices=STATUS_CHOICES, default=NEW_STATUS)
    change = models.DateTimeField(auto_now=True, verbose_name=u'Last change')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name=u'User')

    def __str__(self):
        return self.STATUS_CHOICES[self.status][1]

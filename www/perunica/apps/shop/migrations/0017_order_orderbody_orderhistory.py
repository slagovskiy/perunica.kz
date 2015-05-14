# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0016_goodsgroup_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('fio', models.CharField(default='', verbose_name='Name', max_length=255)),
                ('phone', models.CharField(default='', verbose_name='Phone', max_length=255)),
                ('email', models.CharField(default='', verbose_name='Phone', max_length=255)),
                ('address', models.CharField(default='', verbose_name='Address', max_length=255)),
                ('payment', models.SmallIntegerField(choices=[(1, 'Наличные'), (2, 'Карта')], default=1, verbose_name='Payment')),
                ('date', models.DateTimeField(verbose_name='Added', auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderBody',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('count', models.FloatField(default=0, verbose_name='Count')),
                ('change', models.DateTimeField(verbose_name='Last change', auto_now=True)),
                ('goods', models.ForeignKey(to='shop.Goods')),
                ('option1', models.ForeignKey(related_name='o1', blank=True, to='shop.Goods')),
                ('option2', models.ForeignKey(related_name='o2', blank=True, to='shop.Goods')),
                ('option3', models.ForeignKey(related_name='o3', blank=True, to='shop.Goods')),
                ('order', models.ForeignKey(to='shop.Order')),
                ('user', models.ForeignKey(blank=True, null=True, verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Новый'), (2, 'Готовится'), (3, 'Доставляется'), (4, 'Выдан')], default=1, verbose_name='Status')),
                ('change', models.DateTimeField(verbose_name='Last change', auto_now=True)),
                ('order', models.ForeignKey(to='shop.Order')),
                ('user', models.ForeignKey(blank=True, null=True, verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_menu_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', max_length=255)),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('name', models.TextField(verbose_name='Name', max_length=255)),
                ('menu', models.ForeignKey(to='shop.Menu')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Sub menu',
                'verbose_name_plural': 'Sub menu',
            },
        ),
    ]

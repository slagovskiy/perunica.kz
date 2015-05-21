# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perunica.apps.shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_menu_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='banner',
            field=models.ImageField(upload_to=perunica.apps.shop.models.Menu.upload_to, null=True, verbose_name='Banner', blank=True),
        ),
    ]

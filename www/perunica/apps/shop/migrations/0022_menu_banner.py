# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perunica.apps.shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20150519_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='banner',
            field=models.ImageField(null=True, upload_to=perunica.apps.shop.models.Menu.upload_to, verbose_name='Banner'),
        ),
    ]

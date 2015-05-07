# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perunica.apps.shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_goodslinkgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.ImageField(verbose_name='Icon', upload_to=perunica.apps.shop.models.Menu.upload_to, null=True),
        ),
    ]

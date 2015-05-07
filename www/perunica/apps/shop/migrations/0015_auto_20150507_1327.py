# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perunica.apps.shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20150507_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to=perunica.apps.shop.models.Goods.upload_to, verbose_name='Image'),
        ),
    ]

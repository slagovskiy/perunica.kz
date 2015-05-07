# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perunica.apps.shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20150507_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(null=True, upload_to=perunica.apps.shop.models.Goods.upload_to, verbose_name='Image'),
        ),
    ]

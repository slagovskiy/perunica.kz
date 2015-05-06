# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='icon',
            field=models.ImageField(null=True, verbose_name='Icon', upload_to='menu_icons'),
        ),
    ]

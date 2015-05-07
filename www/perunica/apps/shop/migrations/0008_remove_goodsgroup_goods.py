# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_goodsgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsgroup',
            name='goods',
        ),
    ]

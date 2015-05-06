# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150506_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='sub_menu',
            field=models.ForeignKey(to='shop.SubMenu', null=True, blank=True),
        ),
    ]

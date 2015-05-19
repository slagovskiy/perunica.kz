# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20150515_1408'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Manager',
        ),
    ]

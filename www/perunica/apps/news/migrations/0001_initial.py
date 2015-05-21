# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('date', models.DateTimeField(verbose_name='Date', auto_now_add=True)),
                ('title', models.CharField(default='', max_length=255, verbose_name='Title')),
                ('message', models.TextField(default='', blank=True, verbose_name='Message', null=True)),
            ],
        ),
    ]

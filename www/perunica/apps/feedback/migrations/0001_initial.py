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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('deleted', models.BooleanField(verbose_name='Deleted', default=False)),
                ('allowed', models.BooleanField(verbose_name='Allowed', default=False)),
                ('date', models.DateTimeField(verbose_name='Date', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255, default='')),
                ('email', models.EmailField(blank=True, null=True, verbose_name='Email', max_length=255, default='')),
                ('phone', models.CharField(blank=True, null=True, verbose_name='Phone', max_length=255, default='')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment', max_length=2048, default='')),
            ],
        ),
    ]

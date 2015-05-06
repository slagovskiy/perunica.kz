# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20150506_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('deleted', models.BooleanField(verbose_name='Deleted', default=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Units',
                'ordering': ['name'],
                'verbose_name': 'Unit',
            },
        ),
        migrations.AlterField(
            model_name='goods',
            name='unit',
            field=models.ForeignKey(to='shop.Unit'),
        ),
    ]

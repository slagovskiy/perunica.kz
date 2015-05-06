# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_submenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(verbose_name='Deleted', default=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('image', models.ImageField(verbose_name='Image', upload_to='goods', null=True)),
                ('description', models.TextField(verbose_name='Description', max_length=1024)),
                ('weight', models.IntegerField(verbose_name='Weight', default=0)),
                ('unit', models.CharField(verbose_name='Unit', max_length=10, default='гр.')),
                ('price', models.FloatField(verbose_name='Price', default=0)),
                ('is_new', models.BooleanField(verbose_name='New', default=False)),
                ('is_sticked', models.BooleanField(verbose_name='Sticked on top', default=False)),
                ('is_on_first', models.BooleanField(verbose_name='On first', default=False)),
            ],
            options={
                'verbose_name': 'Goods',
                'ordering': ['menu', 'is_sticked', 'is_new', 'name'],
                'verbose_name_plural': 'Goods',
            },
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=255),
        ),
        migrations.AddField(
            model_name='goods',
            name='menu',
            field=models.ForeignKey(to='shop.Menu'),
        ),
        migrations.AddField(
            model_name='goods',
            name='sub_menu',
            field=models.ForeignKey(to='shop.SubMenu', null=True),
        ),
    ]

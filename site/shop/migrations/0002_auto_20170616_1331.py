# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-16 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='shop.Category', verbose_name='Категория'),
        ),
    ]

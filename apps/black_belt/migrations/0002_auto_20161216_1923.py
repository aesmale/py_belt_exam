# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black_belt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='wishlist',
            field=models.ManyToManyField(to='black_belt.Wishlist'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0003_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='ShoppingCart',
        ),
    ]

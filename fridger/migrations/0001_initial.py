# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-13 11:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quantity', models.PositiveIntegerField()),
                ('item_path', models.ImageField(upload_to='food_items/')),
                ('item_path2', models.ImageField(null=True, upload_to='food_items/')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('supply_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_path', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_qty', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.Product')),
            ],
        ),
    ]

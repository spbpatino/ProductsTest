# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productsreferences',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

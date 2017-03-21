# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 15:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20160613_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=b'2017-03-21', max_length=200)),
                ('obert', models.BooleanField(default=True)),
                ('data', models.DateField(default=datetime.date(2017, 3, 21))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitat', models.FloatField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Carrito')),
                ('producte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
    ]

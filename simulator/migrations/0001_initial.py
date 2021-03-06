# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 05:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('current_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('last_time_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('quantity_purchased', models.PositiveIntegerField()),
                ('price_purchased', models.DecimalField(decimal_places=3, max_digits=10)),
                ('date_purchased', models.DateTimeField()),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instrument', to='simulator.Instrument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

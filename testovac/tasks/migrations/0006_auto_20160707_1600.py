# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-07 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('tasks', '0005_auto_20160705_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='administrators_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='administrators_of_competition', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='users_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_of_competition', to='auth.Group'),
        ),
    ]

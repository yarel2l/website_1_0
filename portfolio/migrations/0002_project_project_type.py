# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-06 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ManyToManyField(db_table='website_services_projects', related_name='services_projects_related', to='services.Service'),
        ),
    ]

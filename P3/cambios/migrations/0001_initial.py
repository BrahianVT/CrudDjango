# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-02-23 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(help_text='Indica descripcion')),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media/imagenes')),
            ],
        ),
    ]
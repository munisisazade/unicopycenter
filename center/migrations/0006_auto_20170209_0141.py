# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0005_uploads_relation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploads',
            options={'ordering': ('-id',), 'verbose_name': 'Print olunacaq fayllar', 'verbose_name_plural': 'Print olunacaq fayllar'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ad və Soyadı'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='group',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Qrup'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='kurs',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Kurs'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomre'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Əlavə məlumat'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='universitet',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Universitet'),
        ),
    ]

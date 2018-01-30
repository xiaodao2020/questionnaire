# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='role',
            field=models.ManyToManyField(null=True, to='app01.Role', verbose_name='担任的角色'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=16, verbose_name='角色名'),
        ),
    ]
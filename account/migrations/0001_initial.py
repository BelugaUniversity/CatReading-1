# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-06 01:36
from __future__ import unicode_literals

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userName', models.CharField(max_length=30, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('is_active', models.BooleanField(default=True)),
                ('registerTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('adminType', models.IntegerField(default=0)),
                ('resetPasswordToken', models.CharField(blank=True, max_length=40, null=True)),
                ('resetPasswordTokenCreateTime', models.DateTimeField(blank=True, null=True)),
                ('isForbidden', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendTicket', models.IntegerField(default=0, verbose_name='\u63a8\u8350\u7968')),
                ('diamondTicket', models.IntegerField(default=0, verbose_name='\u94bb\u77f3\u7968')),
                ('balance', models.IntegerField(default=0, verbose_name='\u732b\u5e01\u4f59\u989d')),
                ('lastReadBook', models.IntegerField(default=0, verbose_name='\u6700\u8fd1\u9605\u8bfb\u4e66\u7c4dId')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

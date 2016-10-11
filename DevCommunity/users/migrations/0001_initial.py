# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreUser',
            fields=[
                ('user_no', models.PositiveIntegerField(serialize=False, primary_key=True, db_column='user_no')),
                ('name', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address', db_column='email')),
                ('password', models.CharField(max_length=128, db_column='password')),
                ('profile_img', models.CharField(max_length=100, db_column='profile_img')),
                ('job', models.CharField(max_length=10, db_column='job')),
                ('gender', models.CharField(max_length=5, db_column='gender')),
                ('admin_yn', models.BooleanField(default=False, db_column='admin_yn')),
                ('login_yn', models.BooleanField(default=False, db_column='login_yn')),
                ('create_datetime', models.BooleanField(default=False, db_column='create_datetime')),
                ('last_login_datetime', models.BooleanField(default=False, db_column='last_login')),
            ],
        ),
    ]

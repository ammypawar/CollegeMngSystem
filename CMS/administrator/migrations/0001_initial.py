# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_no', models.IntegerField()),
                ('uni_soc_name', models.CharField(max_length=100)),
                ('institute_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(default=b'')),
                ('url', models.URLField(help_text=b'e.g. http://www.something@example.com (optional)', blank=True)),
            ],
        ),
    ]

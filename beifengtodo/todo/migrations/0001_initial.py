# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ptime', models.DateTimeField(auto_now=True, verbose_name='\u8bb0\u5f55\u65f6\u95f4', auto_created=True)),
                ('content', models.CharField(max_length=400, verbose_name='\u5f85\u529e\u4e8b\u9879')),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '\u4ee3\u529e\u4e8b\u9879\u8868',
            },
        ),
    ]

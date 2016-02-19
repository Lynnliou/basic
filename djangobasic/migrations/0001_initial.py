# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_context', models.TextField(verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6')),
                ('event_time', models.DateTimeField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('event_state', models.BooleanField(default=False, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
            options={
                'db_table': 'event',
                'verbose_name': '\u4e8b\u4ef6',
                'verbose_name_plural': '\u4e8b\u4ef6',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangobasic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='update_time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]

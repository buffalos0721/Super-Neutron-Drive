# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20150103_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='cancelled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

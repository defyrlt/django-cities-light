# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20150206_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='district',
            field=models.CharField(db_index=True, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]

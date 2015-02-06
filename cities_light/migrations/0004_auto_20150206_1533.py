# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_language'),
        ('cities_light', '0003_auto_20141002_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='language',
            field=models.ForeignKey(default=1, to='core.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='language',
            field=models.ForeignKey(default=1, to='core.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='language',
            field=models.ForeignKey(default=1, to='core.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesregion',
            name='language',
            field=models.ForeignKey(default=1, to='core.Language'),
            preserve_default=False,
        ),
    ]

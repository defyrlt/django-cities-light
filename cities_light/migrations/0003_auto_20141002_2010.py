# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0002_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_ascii', models.CharField(db_index=True, max_length=200, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('geoname_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('alternate_names', models.TextField(default=b'', null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('display_name', models.CharField(max_length=200)),
                ('geoname_code', models.CharField(db_index=True, max_length=50, null=True, blank=True)),
                ('city', models.ManyToManyField(to='cities_light.City', blank=True)),
                ('country', models.ManyToManyField(to='cities_light.Country', blank=True)),
                ('region', models.ManyToManyField(to='cities_light.Region', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name': 'Sales region',
                'verbose_name_plural': 'Sales regions',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='region',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('country', 'name', 'deleted'), ('country', 'slug', 'deleted')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_origin', models.CharField(max_length=255)),
                ('zoom', models.IntegerField(default=1)),
                ('resourceType', models.CharField(default=b'Communities', max_length=255, choices=[(b'layer', b'Layer'), (b'maps', b'Maps'), (b'communities', b'Communities'), (b'geoprojects', b'GeoProjects')])),
                ('coordinates', models.CharField(default=b'', max_length=1000)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20150813_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSitemapProperties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('changefreq', models.CharField(max_length=20, verbose_name='Change frequency', choices=[(b'yearly', 'yearly'), (b'hourly', 'hourly'), (b'monthly', 'monthly'), (b'always', 'always'), (b'never', 'never'), (b'daily', 'daily'), (b'weekly', 'weekly')])),
                ('priority', models.DecimalField(verbose_name='Priority', max_digits=2, decimal_places=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('public_extension', models.OneToOneField(related_name='draft_extension', null=True, editable=False, to='djangocms_page_sitemap.PageSitemapProperties')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

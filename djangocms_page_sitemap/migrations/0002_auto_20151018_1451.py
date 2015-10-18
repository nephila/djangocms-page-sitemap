# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_page_sitemap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesitemapproperties',
            name='include_in_sitemap',
            field=models.BooleanField(default=True, verbose_name='Include in sitemap'),
        ),
        migrations.AlterField(
            model_name='pagesitemapproperties',
            name='changefreq',
            field=models.CharField(max_length=20, choices=[('daily', 'daily'), ('yearly', 'yearly'), ('never', 'never'), ('always', 'always'), ('hourly', 'hourly'), ('weekly', 'weekly'), ('monthly', 'monthly')], verbose_name='Change frequency'),
        ),
    ]

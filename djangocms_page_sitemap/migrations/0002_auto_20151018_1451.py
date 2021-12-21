from django.db import migrations, models
from djangocms_page_sitemap.settings import PAGE_SITEMAP_CHANGEFREQ_LIST


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
            field=models.CharField(max_length=20, choices=PAGE_SITEMAP_CHANGEFREQ_LIST.items(), verbose_name='Change frequency'),
        ),
    ]

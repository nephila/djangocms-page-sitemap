import django.core.validators
from django.db import migrations, models

from djangocms_page_sitemap.settings import PAGE_SITEMAP_CHANGEFREQ_LIST


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_page_sitemap", "0002_auto_20151018_1451"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagesitemapproperties",
            name="changefreq",
            field=models.CharField(
                max_length=20,
                verbose_name="Change frequency",
                default="monthly",
                choices=PAGE_SITEMAP_CHANGEFREQ_LIST.items(),
            ),
        ),
        migrations.AlterField(
            model_name="pagesitemapproperties",
            name="priority",
            field=models.DecimalField(
                max_digits=2,
                decimal_places=1,
                default=0.5,
                verbose_name="Priority",
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1),
                ],
            ),
        ),
    ]

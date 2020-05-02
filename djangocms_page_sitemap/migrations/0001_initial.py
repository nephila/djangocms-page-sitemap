import django.core.validators
from django.db import migrations, models

from djangocms_page_sitemap.settings import PAGE_SITEMAP_CHANGEFREQ_LIST


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="PageSitemapProperties",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "changefreq",
                    models.CharField(
                        max_length=20,
                        verbose_name="Change frequency",
                        choices=PAGE_SITEMAP_CHANGEFREQ_LIST.items(),
                    ),
                ),
                (
                    "priority",
                    models.DecimalField(
                        verbose_name="Priority",
                        max_digits=2,
                        decimal_places=1,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(1),
                        ],
                    ),
                ),
                (
                    "extended_object",
                    models.OneToOneField(editable=False, to="cms.Page", on_delete=models.CASCADE),
                ),
                (
                    "public_extension",
                    models.OneToOneField(
                        related_name="draft_extension",
                        null=True,
                        editable=False,
                        to="djangocms_page_sitemap.PageSitemapProperties",
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

from django.contrib.sitemaps.views import sitemap
from django.urls import re_path

from .sitemap import ExtendedSitemap

urlpatterns = [
    re_path(r"^sitemap\.xml$", sitemap, {"sitemaps": {"cmspages": ExtendedSitemap}}),
]

from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemap import ExtendedSitemap

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": ExtendedSitemap}}),
]

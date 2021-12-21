
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from .sitemap import ExtendedSitemap

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': ExtendedSitemap}}),
]

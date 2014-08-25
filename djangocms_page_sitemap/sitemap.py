# -*- coding: utf-8 -*-
from cms.sitemaps import CMSSitemap
from .models import PageSitemapProperties


class ExtendedSitemap(CMSSitemap):
    default_changefreq = CMSSitemap.changefreq
    default_priority = CMSSitemap.priority

    def priority(self, title):
        try:
            return title.page.pagesitemapproperties.priority
        except PageSitemapProperties.DoesNotExist:
            return self.default_priority

    def changefreq(self, title):
        try:
            return title.page.pagesitemapproperties.changefreq
        except PageSitemapProperties.DoesNotExist:
            return self.default_changefreq

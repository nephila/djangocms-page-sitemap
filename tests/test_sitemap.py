# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.cache import cache
from django.utils.timezone import now
from djangocms_page_sitemap.models import PageSitemapProperties
from djangocms_page_sitemap.sitemap import ExtendedSitemap
from djangocms_page_sitemap.utils import get_cache_key

from .base import BaseTest


class SitemapTest(BaseTest):

    def test_sitemap_base(self):
        test_string = '<url><loc>http://example.com/it/</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>' % now().strftime('%Y-%m-%d')
        self.get_pages()
        sitemap = self.client.get('/sitemap.xml')
        self.assertContains(sitemap, test_string)

    def test_sitemap_extended(self):
        test_string = '<url><loc>http://example.com/it/</loc><lastmod>%s</lastmod><changefreq>never</changefreq><priority>0.2</priority></url>' % now().strftime('%Y-%m-%d')
        page1, page2 = self.get_pages()
        PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never')
        page1.publish('it')
        sitemap = self.client.get('/sitemap.xml')
        self.assertContains(sitemap, test_string)

    def test_sitemap_cache(self):
        page1, page2 = self.get_pages()
        PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never')
        PageSitemapProperties.objects.create(
            extended_object=page2, priority='0.8', changefreq='hourly')
        page1.publish('it')
        page1 = page1.get_public_object()
        page2.publish('it')
        page2 = page2.get_public_object()
        sitemap = ExtendedSitemap()
        self.assertEqual(len(sitemap.items()), 4)
        for item in sitemap.items():
            if item.page.pk == page1.pk:
                self.assertEqual(sitemap.changefreq(item), 'never')
                ext_key = get_cache_key(item.page)
                self.assertEqual(cache.get(ext_key), item.page.pagesitemapproperties)
            if item.page.pk == page2.pk:
                self.assertEqual(sitemap.changefreq(item), 'hourly')

        ext_key = get_cache_key(page1)
        page1.pagesitemapproperties.save()
        self.assertEqual(cache.get(ext_key), None)

        ext_key = get_cache_key(page2)
        page2.delete()
        self.assertEqual(cache.get(ext_key), None)

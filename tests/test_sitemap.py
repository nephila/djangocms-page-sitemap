# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from decimal import Decimal
from unittest import skipIf

from cms.api import create_page, create_title

from django.core.cache import cache
from django.utils.timezone import now

from djangocms_page_sitemap.models import PageSitemapProperties
from djangocms_page_sitemap.sitemap import ExtendedSitemap
from djangocms_page_sitemap.utils import get_cache_key, is_versioning_enabled

from .base import BaseTest


class SitemapTest(BaseTest):

    def test_sitemap_base(self):
        page1, page2, page3 = self.get_pages()
        if is_versioning_enabled():
            page1_content = create_title(title='pagecontent1', language='en', page=page1,
                                         created_by=self.user)
            page2_content = create_title(title='pagecontent 2', language='en', page=page2,
                                         created_by=self.user)
            page3_content = create_title(title='pagecontent3', language='en', page=page3,
                                         created_by=self.user)
            page1_content.versions.first().publish(self.user)
            page2_content.versions.first().publish(self.user)
            page3_content.versions.first().publish(self.user)

        sitemap = self.client.get('/sitemap.xml')
        test_string = '<url><loc>http://example.com/%s/</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>' % (page1.get_title_obj().language,now().strftime('%Y-%m-%d'))
        self.assertContains(sitemap, test_string)

    def test_sitemap_extended(self):
        page1, page2, page3 = self.get_pages()
        PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never'
        )
        if is_versioning_enabled():
            page1_content = create_title(title='pagecontent1', language='en', page=page1,
                                         created_by=self.user)
            page2_content = create_title(title='pagecontent 2', language='en', page=page2,
                                         created_by=self.user)
            page3_content = create_title(title='pagecontent3', language='en', page=page3,
                                         created_by=self.user)
            page1_content.versions.first().publish(self.user)
            page2_content.versions.first().publish(self.user)
            page3_content.versions.first().publish(self.user)

        test_string = '<url><loc>http://example.com/%s/</loc><lastmod>%s</lastmod><changefreq>never</changefreq><priority>0.2</priority></url>' % (page1.get_title_obj().language,now().strftime('%Y-%m-%d'))
        sitemap = self.client.get('/sitemap.xml')
        self.assertContains(sitemap, test_string)

    def test_sitemap_exclude(self):
        page1, page2, page3 = self.get_pages()
        if is_versioning_enabled():
            page1_content = create_title(title='pagecontent1', language='en', page=page1,
                                         created_by=self.user)
            page2_content = create_title(title='pagecontent 2', language='en', page=page2,
                                         created_by=self.user)
            page3_content = create_title(title='pagecontent3', language='en', page=page3,
                                         created_by=self.user)
            page1_content.versions.first().publish(self.user)
            page2_content.versions.first().publish(self.user)
            page3_content.versions.first().publish(self.user)

        PageSitemapProperties.objects.create(
            extended_object=page3, priority='0.2', changefreq='never', include_in_sitemap=False
        )
        sitemap = ExtendedSitemap()
        # unpublished since change, still in the sitemap
        self.assertEqual(len(sitemap.items()), 4)
        sitemap = ExtendedSitemap()
        # published, then no longer in the sitemap
        self.assertEqual(len(sitemap.items()), 4)

    def test_sitemap_cache(self):
        page1, page2, page3 = self.get_pages()
        if is_versioning_enabled():
            page1_content = create_title(title='pagecontent1', language='en', page=page1,
                                         created_by=self.user)
            page2_content = create_title(title='pagecontent 2', language='en', page=page2,
                                         created_by=self.user)
            page3_content = create_title(title='pagecontent3', language='en', page=page3,
                                         created_by=self.user)
            page1_content.versions.first().publish(self.user)
            page2_content.versions.first().publish(self.user)
            page3_content.versions.first().publish(self.user)
        PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never'
        )
        PageSitemapProperties.objects.create(
            extended_object=page3, priority='0.8', changefreq='hourly'
        )
        sitemap = ExtendedSitemap()
        self.assertEqual(len(sitemap.items()), 6)
        for item in sitemap.items():
            if item.page.pk == page1.pk:
                self.assertEqual(sitemap.changefreq(item), 'never')
                self.assertEqual(sitemap.priority(item), Decimal('0.2'))
                ext_key = get_cache_key(item.page)
                self.assertEqual(cache.get(ext_key), item.page.pagesitemapproperties)
            if item.page.pk == page3.pk:
                self.assertEqual(sitemap.changefreq(item), 'hourly')
                self.assertEqual(sitemap.priority(item), Decimal('0.8'))

        ext_key = get_cache_key(page1)
        page1.pagesitemapproperties.save()
        self.assertEqual(cache.get(ext_key), None)

        ext_key = get_cache_key(page3)
        page3.delete()
        self.assertEqual(cache.get(ext_key), None)

    @skipIf(not is_versioning_enabled(), 'This test can only run when versioning is installed')
    def test_pageurl_lastmod_with_cms4_versioning(self):
        # Check the latest version modified date for the page is checked for lastmod()
        # if versioning is enabled, Currenly test is skipped , as this may require changes in testsuite
        page_1 = create_page('page-one', 'page.html', language='en', created_by=self.user)
        page_content = create_title(title='page un', language='en', page=page_1, created_by=self.user)
        if is_versioning_enabled():
            page_content.versions.first().publish(self.user)
        last_modified_date = '<lastmod>%s</lastmod>' % (
            page_content.versions.first().modified.strftime('%Y-%m-%d')
        )
        expected_string = '<url><loc>http://example.com%s</loc>%s<changefreq>monthly</changefreq><priority>0.5</priority></url>' % (page_1.get_absolute_url(language='en'), last_modified_date)
        sitemap = self.client.get('/sitemap.xml')

        self.assertContains(sitemap, expected_string)

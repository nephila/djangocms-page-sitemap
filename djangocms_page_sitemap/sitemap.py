
from __future__ import absolute_import, print_function, unicode_literals

from collections import defaultdict

from cms.models import PageContent, PageUrl
from cms.sitemaps import CMSSitemap
from cms.utils import get_current_site
from cms.utils.i18n import get_public_languages
from django.core.cache import cache
from django.db.models import Prefetch

from .models import PageSitemapProperties
from .settings import PAGE_SITEMAP_CACHE_DURATION, PAGE_SITEMAP_DEFAULT_CHANGEFREQ
from .utils import get_cache_key, is_versioning_enabled


class ExtendedSitemap(CMSSitemap):
    default_changefreq = PAGE_SITEMAP_DEFAULT_CHANGEFREQ
    default_priority = CMSSitemap.priority

    def items(self):
        # FIXME:This method was created from this commit:
        # https://github.com/divio/django-cms/blob/2894ae8bcf92092d947a097499c01ab2bbb0e6df/cms/sitemaps/cms_sitemap.py
        site = get_current_site()
        languages = get_public_languages(site_id=site.pk)
        page_content_prefetch = Prefetch(
            'page__pagecontent_set',
            queryset=PageContent.objects.filter(
                language__in=languages,
            )
        )
        all_urls = (
            PageUrl
                .objects
                .get_for_site(site)
                .prefetch_related(page_content_prefetch)
                .filter(
                language__in=languages,
                path__isnull=False,
                page__login_required=False,
                page__node__site=site,
            )
                .exclude(page__pagesitemapproperties__include_in_sitemap=False)
                .order_by('page__node__path')
        )
        valid_urls = []
        for page_url in all_urls:
            for page_content in page_url.page.pagecontent_set.all():
                if page_url.language == page_content.language:
                    valid_urls.append(page_url)
                    break

        return valid_urls

    def priority(self, title):
        ext_key = get_cache_key(title.page)
        properties = cache.get(ext_key)
        if properties:
            return properties.priority
        else:
            try:
                cache.set(ext_key, title.page.pagesitemapproperties, PAGE_SITEMAP_CACHE_DURATION)
                return title.page.pagesitemapproperties.priority
            except PageSitemapProperties.DoesNotExist:
                return self.default_priority

    def changefreq(self, title):
        ext_key = get_cache_key(title.page)
        properties = cache.get(ext_key)
        if properties:  # pragma: no cover
            return properties.changefreq
        else:
            try:
                cache.set(ext_key, title.page.pagesitemapproperties, PAGE_SITEMAP_CACHE_DURATION)
                return title.page.pagesitemapproperties.changefreq
            except PageSitemapProperties.DoesNotExist:
                return self.default_changefreq

    def lastmod(self, page_url):
        # if versioning is enabled we  return the latest version modified using the versioning
        # modified date. if versioning is disabled we return the page changed_date
        if is_versioning_enabled():
            site = get_current_site()
            page_contents = PageContent.objects.filter(
                page=page_url.page,
                language=page_url.language,
                page__node__site=site,
            ).first()

            if page_contents:
                published_version = page_contents.versions.first()
                return published_version.modified

        return page_url.page.changed_date

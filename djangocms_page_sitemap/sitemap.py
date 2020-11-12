from cms.sitemaps import CMSSitemap
from django.core.cache import cache

from .models import PageSitemapProperties
from .settings import PAGE_SITEMAP_CACHE_DURATION, PAGE_SITEMAP_DEFAULT_CHANGEFREQ
from .utils import get_cache_key


class ExtendedSitemap(CMSSitemap):
    default_changefreq = PAGE_SITEMAP_DEFAULT_CHANGEFREQ
    default_priority = CMSSitemap.priority

    def items(self):
        return super().items().exclude(page__pagesitemapproperties__include_in_sitemap=False)

    def priority(self, title):
        ext_key = get_cache_key(title.page)
        properties = cache.get(ext_key)
        if properties:
            return properties.priority
        else:
            try:
                cache.set(
                    ext_key,
                    title.page.pagesitemapproperties,
                    PAGE_SITEMAP_CACHE_DURATION,
                )
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
                cache.set(
                    ext_key,
                    title.page.pagesitemapproperties,
                    PAGE_SITEMAP_CACHE_DURATION,
                )
                return title.page.pagesitemapproperties.changefreq
            except PageSitemapProperties.DoesNotExist:
                return self.default_changefreq

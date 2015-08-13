# -*- coding: utf-8 -*-


def get_cache_key(page):
    """
    Create the cache key for the current page and language
    """
    try:
        from cms.cache import _get_cache_key
    except ImportError:
        from cms.templatetags.cms_tags import _get_cache_key
    site_id = page.site_id
    return _get_cache_key('page_sitemap', page, 'default', site_id)

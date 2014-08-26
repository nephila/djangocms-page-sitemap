# -*- coding: utf-8 -*-


def get_cache_key(page):
    """
    Create the cache key for the current page and language
    """
    from cms.templatetags.cms_tags import _get_cache_key
    site_id = page.site_id
    return _get_cache_key('page_sitemap', page, 'default', site_id)
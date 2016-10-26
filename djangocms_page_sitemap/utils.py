# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.cache import _get_cache_key


def get_cache_key(page):
    """
    Create the cache key for the current page and language
    """
    site_id = page.site_id
    return _get_cache_key('page_sitemap', page, 'default', site_id)

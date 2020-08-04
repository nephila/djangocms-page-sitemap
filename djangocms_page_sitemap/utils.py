# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.apps import apps

from cms.cache import _get_cache_key


def get_cache_key(page):
    """
    Create the cache key for the current page and language
    """
    try:
        site_id = page.node.site_id
    except AttributeError:
        site_id = page.site_id
    return _get_cache_key('page_sitemap', page, 'default', site_id)


def is_versioning_enabled():
    from cms.models import PageContent
    try:
        app_config = apps.get_app_config('djangocms_versioning')
        return app_config.cms_extension.is_content_model_versioned(PageContent)
    except LookupError:
        return False

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from cms.utils import get_cms_setting
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

PAGE_SITEMAP_CHANGEFREQ_DEFAULT_LIST = {
    'always': _('always'),
    'hourly': _('hourly'),
    'daily': _('daily'),
    'weekly': _('weekly'),
    'monthly': _('monthly'),
    'yearly': _('yearly'),
    'never': _('never'),
}
PAGE_SITEMAP_CHANGEFREQ_LIST = getattr(
    settings, 'PAGE_SITEMAP_CHANGEFREQ_LIST', PAGE_SITEMAP_CHANGEFREQ_DEFAULT_LIST
)
PAGE_SITEMAP_DEFAULT_CHANGEFREQ = getattr(
    settings, 'PAGE_SITEMAP_DEFAULT_CHANGEFREQ', CMSSitemap.changefreq
)
PAGE_SITEMAP_CACHE_DURATION = get_cms_setting('CACHE_DURATIONS')['menus']

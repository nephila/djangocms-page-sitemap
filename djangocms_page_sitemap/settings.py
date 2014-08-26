# -*- coding: utf-8 -*-
from cms.utils import get_cms_setting
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

PAGE_SITEMAP_CHANGEFREQ_DEFAULT = {
    'always': _(u'always'),
    'hourly': _(u'hourly'),
    'daily': _(u'daily'),
    'weekly': _(u'weekly'),
    'monthly': _(u'monthly'),
    'yearly': _(u'yearly'),
    'never': _(u'never'),
}
PAGE_SITEMAP_CHANGEFREQ = getattr(settings, 'PAGE_SITEMAP_CHANGEFREQ', PAGE_SITEMAP_CHANGEFREQ_DEFAULT)
PAGE_SITEMAP_CACHE = get_cms_setting('CACHE_DURATIONS')['menus']

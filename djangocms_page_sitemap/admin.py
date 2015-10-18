# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.extensions import PageExtensionAdmin
from django.contrib import admin

from .models import PageSitemapProperties


class PageSitemapPropertiesAdmin(PageExtensionAdmin):
    pass
admin.site.register(PageSitemapProperties, PageSitemapPropertiesAdmin)

from cms.extensions import PageExtensionAdmin
from django.contrib import admin

from .models import PageSitemapProperties


@admin.register(PageSitemapProperties)
class PageSitemapPropertiesAdmin(PageExtensionAdmin):
    pass

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.extensions import PageExtension, extension_pool
from cms.models import Page
from cms.utils.compat.dj import python_2_unicode_compatible
from django.core.cache import cache
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from .settings import PAGE_SITEMAP_CHANGEFREQ_LIST
from .utils import get_cache_key


@extension_pool.register
@python_2_unicode_compatible
class PageSitemapProperties(PageExtension):
    changefreq = models.CharField(_('Change frequency'), max_length=20, default='monthly',
                                  choices=PAGE_SITEMAP_CHANGEFREQ_LIST.items())
    priority = models.DecimalField(_('Priority'), decimal_places=1,
                                   max_digits=2, default=0.5,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    include_in_sitemap = models.BooleanField(_('Include in sitemap'), default=True)

    def __str__(self):
        return _('Sitemap values for Page %s') % self.extended_object.pk


# Cache cleanup when deleting pages / editing page extensions
@receiver(pre_delete, sender=Page)
def cleanup_page(sender, instance, **kwargs):
    key = get_cache_key(instance)
    cache.delete(key)


@receiver(post_save, sender=PageSitemapProperties)
def cleanup_pagemeta(sender, instance, **kwargs):
    key = get_cache_key(instance.extended_object)
    cache.delete(key)

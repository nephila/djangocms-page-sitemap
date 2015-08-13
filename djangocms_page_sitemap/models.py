# -*- coding: utf-8 -*-
from cms.extensions import PageExtension, extension_pool
from cms.models import Page
from cms.utils.compat.dj import python_2_unicode_compatible
from django.core.cache import cache
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from .settings import PAGE_SITEMAP_CHANGEFREQ
from .utils import get_cache_key


@python_2_unicode_compatible
class PageSitemapProperties(PageExtension):
    changefreq = models.CharField(_(u'Change frequency'), max_length=20,
                                  choices=PAGE_SITEMAP_CHANGEFREQ.items())
    priority = models.DecimalField(_(u'Priority'), decimal_places=1,
                                   max_digits=2,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return _(u'Sitemap values for Page %s') % self.extended_object.pk
extension_pool.register(PageSitemapProperties)


# Cache cleanup when deleting pages / editing page extensions
@receiver(pre_delete, sender=Page)
def cleanup_page(sender, instance, **kwargs):
    key = get_cache_key(instance)
    cache.delete(key)


@receiver(post_save, sender=PageSitemapProperties)
def cleanup_pagemeta(sender, instance, **kwargs):
    key = get_cache_key(instance.extended_object)
    cache.delete(key)

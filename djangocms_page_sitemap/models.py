from cms.extensions import PageExtension, extension_pool
from cms.models import Page
from django.core.cache import cache
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from .settings import PAGE_SITEMAP_CHANGEFREQ_LIST
from .utils import get_cache_key


@extension_pool.register
class PageSitemapProperties(PageExtension):
    changefreq = models.CharField(
        _('Change frequency'), max_length=20, default='monthly',
        choices=PAGE_SITEMAP_CHANGEFREQ_LIST.items()
    )
    priority = models.DecimalField(
        _('Priority'), decimal_places=1, max_digits=2, default=0.5,
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    include_in_sitemap = models.BooleanField(_('Include in sitemap'), default=True)
    noindex = models.BooleanField(
        _('Mark as no index'), default=False,
        help_text=_('Add meta tag robots with value noindex')
    )
    noarchive = models.BooleanField(
        _('Mark as no archive'), default=False,
        help_text=_('Add meta tag robots with value noarchive')
    )
    robots_extra = models.CharField(
        _('Extra robots value'), default='', max_length=200, blank=True,
        help_text=_('Extra values for robots meta tag')
    )

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

from cms.cache import _get_cache_key
from django.apps import apps


def get_cache_key(page):
    """
    Create the cache key for the current page and language
    """
    site_id = page.node.site_id
    return _get_cache_key("page_sitemap", page, "default", site_id)


def is_versioning_enabled():
    """Check if djangocms-versioning plugin is installed."""
    try:
        from cms.models import PageContent

        try:
            app_config = apps.get_app_config("djangocms_versioning")
            return app_config.cms_extension.is_content_model_versioned(PageContent)
        except LookupError:  # pragma: no cover
            return False
    except ImportError:
        return False

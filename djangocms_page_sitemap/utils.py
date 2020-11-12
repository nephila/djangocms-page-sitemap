from cms.cache import _get_cache_key


def get_cache_key(page):
    """
    Create the cache key for the current page and language
    """
    site_id = page.node.site_id
    return _get_cache_key("page_sitemap", page, "default", site_id)

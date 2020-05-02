from cms.cache import _get_cache_key


def get_cache_key(page):
    """
    Create the cache key for the current page and language
    """
    try:
        site_id = page.node.site_id
    except AttributeError:
        site_id = page.site_id
    return _get_cache_key("page_sitemap", page, "default", site_id)

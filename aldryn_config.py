try:
    from divio_cli import forms
except ImportError:
    from aldryn_client import forms

PAGE_SITEMAP_CHANGEFREQ_DEFAULT_LIST = {
    "always": "always",
    "hourly": "hourly",
    "daily": "daily",
    "weekly": "weekly",
    "monthly": "monthly",
    "yearly": "yearly",
    "never": "never",
}


class Form(forms.BaseForm):
    PAGE_SITEMAP_DEFAULT_CHANGEFREQ = forms.SelectField(
        "Default changefrequency (default: django CMS value -monthly-)",
        choices=list(PAGE_SITEMAP_CHANGEFREQ_DEFAULT_LIST.items()),
    )
    PAGE_SITEMAP_CACHE_DURATION = forms.CharField(
        "Cache duration (default: same as django CMS menu cache)", required=False
    )

    def to_settings(self, data, settings):
        settings["PAGE_SITEMAP_DEFAULT_CHANGEFREQ"] = data["PAGE_SITEMAP_DEFAULT_CHANGEFREQ"]
        settings["PAGE_SITEMAP_CACHE_DURATION"] = data["PAGE_SITEMAP_CACHE_DURATION"]
        settings["ADDON_URLS"].insert(0, "djangocms_page_sitemap.sitemap_urls")
        return settings

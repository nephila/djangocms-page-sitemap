#!/usr/bin/env python


def gettext(s):
    return s


HELPER_SETTINGS = {
    "CACHES": {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        }
    },
    "CMS_CACHE_DURATIONS": {
        "menus": 10,
        "content": 10,
        "permissions": 10,
    },
    "CMS_CONFIRM_VERSION4": True,
    "ROOT_URLCONF": "tests.test_utils.urls",
    "INSTALLED_APPS": [
        "django.contrib.sitemaps",
    ],
    "LANGUAGE_CODE": "en",
    "TIME_ZONE": "UTC",
    "LANGUAGES": (
        ("en", gettext("English")),
        ("fr", gettext("French")),
        ("it", gettext("Italiano")),
    ),
    "CMS_LANGUAGES": {
        1: [
            {
                "code": "en",
                "name": gettext("English"),
                "public": True,
            },
            {
                "code": "it",
                "name": gettext("Italiano"),
                "public": True,
            },
            {
                "code": "fr",
                "name": gettext("French"),
                "public": True,
            },
        ],
        "default": {
            "hide_untranslated": False,
        },
    },
}
try:
    import djangocms_versioning  # noqa: F401

    HELPER_SETTINGS["INSTALLED_APPS"].append("djangocms_versioning")
except ImportError:
    pass


def run():
    from app_helper import runner

    runner.cms("djangocms_page_sitemap")


def setup():
    import sys

    from app_helper import runner

    runner.setup("djangocms_page_sitemap", sys.modules[__name__], use_cms=True)


if __name__ == "__main__":
    run()

if __name__ == "cms_helper":
    # this is needed to run cms_helper in pycharm
    setup()

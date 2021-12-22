#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import sys


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


def gettext(s):
    return s


HELPER_SETTINGS = {
    "SECRET_KEY": "djangocms-page-sitemap-test-suite-key",
    "NOSE_ARGS": [
        "-s",
    ],
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
    "ROOT_URLCONF": "tests.test_utils.urls",
    # FIXME: Django CMS migrtions with Django 2.2 produce an error when
    # running tests, temporarily disabling migrations
    "MIGRATION_MODULES": DisableMigrations(),
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


def run():
    from app_helper import runner
    runner.cms("djangocms_page_sitemap")


def setup():
    from app_helper import runner
    runner.setup("djangocms_page_sitemap", sys.modules[__name__], use_cms=True)


if __name__ == "__main__":
    run()

if __name__ == "cms_helper":
    # this is needed to run cms_helper in pycharm
    setup()

======================
djangocms-page-sitemap
======================

.. image:: https://img.shields.io/pypi/v/djangocms-page-sitemap.svg
        :target: https://pypi.python.org/pypi/djangocms-page-sitemap
        :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/nephila/djangocms-page-sitemap.svg
        :target: https://travis-ci.org/nephila/djangocms-page-sitemap
        :alt: Latest Travis CI build status

.. image:: https://img.shields.io/pypi/dm/djangocms-page-sitemap.svg
        :target: https://pypi.python.org/pypi/djangocms-page-sitemap
        :alt: Monthly downloads

.. image:: https://coveralls.io/repos/nephila/djangocms-page-sitemap/badge.png
        :target: https://coveralls.io/r/nephila/djangocms-page-sitemap
        :alt: Test coverage

django CMS page extension to handle sitemap customization

Support Python version:

* Python 2.6
* Python 2.7
* Python 3.3
* Python 3.4

Supported Django versions:

* Django 1.6
* Django 1.7
* Django 1.8

Supported django CMS versions:

* django CMS 3.x


Quickstart
----------

* Install djangocms-page-sitemap::

    pip install djangocms-page-sitemap

* Add to ``INSTALLED_APPS`` with ``django.contrib.sitemaps``::

    INSTALLED_APPS = [
        ...
        'django.contrib.sitemaps',
        'djangocms_page_sitemap',
    ]

* Add to the urlconf, eventually removing django CMS sitemap::

    from djangocms_page_sitemap.sitemap import ExtendedSitemap

    urlpatterns = patterns('',
        ...
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': ExtendedSitemap}}),
    )

Upgrading
---------

Since version 0.2 ``djangocms-page-sitemap`` ships with migrations both for south and Django 1.7+.

When upgrading you need to fake the migration to avoid errors::

    $ python manage.py migrate djangocms_page_meta --fake


Features
--------

* Support for changefreq and priority customisation per-page
* Values are cached
* django CMS toolbar integration

======================
djangocms-page-sitemap
======================

.. image:: https://pypip.in/v/djangocms-page-sitemap/badge.png
        :target: https://pypi.python.org/pypi/djangocms-page-sitemap
        :alt: Latest PyPI version

.. image:: https://travis-ci.org/nephila/djangocms-page-sitemap.png?branch=master
        :target: https://travis-ci.org/nephila/djangocms-page-sitemap
        :alt: Latest Travis CI build status

.. image:: https://pypip.in/d/djangocms-page-sitemap/badge.png
        :target: https://pypi.python.org/pypi/djangocms-page-sitemap
        :alt: Monthly downloads

.. image:: https://coveralls.io/repos/nephila/djangocms-page-sitemap/badge.png
        :target: https://coveralls.io/r/nephila/djangocms-page-sitemap
        :alt: Test coverage


django CMS page extension to handle sitemap customization


Quickstart
----------

* Install djangocms-page-sitemap::

    pip install djangocms-page-sitemap

* Add to ``INSTALLED_APPS`` with ``django.contrib.sitemaps``::

    INSTALLED_APPS = [
        ...
        'django.contrib.sitemaps',
        'djangocms_page_meta',
    ]

* Add to the urlconf, eventually removing django CMS sitemap::

    from djangocms_page_sitemap.sitemap import ExtendedSitemap

    urlpatterns = patterns('',
        ...
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': ExtendedSitemap}}),
    )

Features
--------

* Support for changefreq and priority customisation per-page
* Values are cached
* django CMS toolbar integration

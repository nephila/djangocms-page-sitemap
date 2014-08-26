======================
djangocms-page-sitemap
======================

.. image:: https://badge.fury.io/py/djangocms-page-sitemap.png
    :target: https://badge.fury.io/py/djangocms-page-sitemap

.. image:: https://travis-ci.org/nephila/djangocms-page-sitemap.png?branch=master
    :target: https://travis-ci.org/nephila/djangocms-page-sitemap

.. image:: https://coveralls.io/repos/nephila/djangocms-page-sitemap/badge.png?branch=master
    :target: https://coveralls.io/r/nephila/djangocms-page-sitemap?branch=master


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
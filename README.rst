======================
djangocms-page-sitemap
======================

.. image:: https://img.shields.io/pypi/v/djangocms-page-sitemap.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-sitemap
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/djangocms-page-sitemap.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-sitemap
    :alt: Monthly downloads

.. image:: https://img.shields.io/pypi/pyversions/djangocms-page-sitemap.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-sitemap
    :alt: Python versions

.. image:: https://img.shields.io/travis/nephila/djangocms-page-sitemap.svg?style=flat-square
    :target: https://travis-ci.org/nephila/djangocms-page-sitemap
    :alt: Latest Travis CI build status

.. image:: https://img.shields.io/coveralls/nephila/djangocms-page-sitemap/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-page-sitemap?branch=master
    :alt: Test coverage

.. image:: https://img.shields.io/codecov/c/github/nephila/djangocms-page-sitemap/develop.svg?style=flat-square
    :target: https://codecov.io/github/nephila/djangocms-page-sitemap
    :alt: Test coverage

.. image:: https://codeclimate.com/github/nephila/djangocms-page-sitemap/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-page-sitemap
   :alt: Code Climate

django CMS page extension to handle sitemap customization

Support Python version:

* Python 2.7, 3.3, 3.4, 3.5

Supported Django versions:

* Django 1.8 to 1.10

Supported django CMS versions:

* django CMS 3.2+


Features
--------

* Support for changefreq and priority customisation per-page
* Option to exclude a page from the Sitemap
* Values are cached
* django CMS toolbar integration


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

* Add the following snippets to the django CMS templates::

    {% load robots_index %}

     ...
    <head>
    <!-- somewhere in the head tag -->
    {% page_robots %}
    </head>
    ...

Usage
-----

After installing as above, you will be able to tune the sitemap setting for each page.

A new menu item ``Sitemap properties`` will be available in the page toolbar.

For each page you will be able to set the following flags / values:

* Sitemap changefreq (default: the django CMS default)
* Sitemap priority (default: 0.5)
* Include page in sitemap (default: `True`)
* Set `noindex` value to page robots meta tag
* Set `noarchite` value to page robots meta tag
* Provide any additional robots meta tag values

 page_robots options
###################

`page_robots` meta tag accepts the following parameters:

* `page`: the page to render robots meta tag (default: current page). Can be
  any valid `page lookup`_
* `site`: the current site id (default: current site).

Settings
--------

* PAGE_SITEMAP_CHANGEFREQ_LIST: List of frequency changes
* PAGE_SITEMAP_DEFAULT_CHANGEFREQ: Default changefrequency (default: django CMS value -monthly-)
* PAGE_SITEMAP_CACHE_DURATION: Cache duration: same as django CMS menu cache)


.. _page lookup: https://docs.django-cms.org/en/reference/templatetags.html#page_lookup

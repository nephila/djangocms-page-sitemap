======================
djangocms-page-sitemap
======================

|Gitter| |PyPiVersion| |PyVersion| |Status| |TestCoverage| |CodeClimate| |License|

django CMS page extension to handle sitemap customization

Support Python version:

* Python 2.7, 3.4, 3.5, 3.6

Supported Django versions:

* Django 1.8 to 1.11

Supported django CMS versions:

* django CMS 3.4+


Features
--------

* Support for changefreq and priority customisation per-page
* Option to exclude a page from the Sitemap
* Values are cached
* django CMS toolbar integration
* Available on Divio Cloud


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


    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        ...
        url(r'^', include(sitemap_urls)),
        ...
    ]

Usage
-----

After installing as above, you will be able to tune the sitemap setting for each page.

A new menu item ``Sitemap properties`` will be available in the page toolbar.

Settings
--------

* PAGE_SITEMAP_CHANGEFREQ_LIST: List of frequency changes
* PAGE_SITEMAP_DEFAULT_CHANGEFREQ: Default changefrequency (default: django CMS value -monthly-)
* PAGE_SITEMAP_CACHE_DURATION: Cache duration: same as django CMS menu cache)



.. |Gitter| image:: https://img.shields.io/badge/GITTER-join%20chat-brightgreen.svg?style=flat-square
    :target: https://gitter.im/nephila/applications
    :alt: Join the Gitter chat

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/djangocms-page-sitemap.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-sitemap
    :alt: Latest PyPI version

.. |PyVersion| image:: https://img.shields.io/pypi/pyversions/djangocms-page-sitemap.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-sitemap
    :alt: Python versions

.. |Status| image:: https://img.shields.io/travis/nephila/djangocms-page-sitemap.svg?style=flat-square
    :target: https://travis-ci.org/nephila/djangocms-page-sitemap
    :alt: Latest Travis CI build status

.. |TestCoverage| image:: https://img.shields.io/coveralls/nephila/djangocms-page-sitemap/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-page-sitemap?branch=master
    :alt: Test coverage

.. |License| image:: https://img.shields.io/github/license/nephila/djangocms-page-sitemap.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djangocms-page-sitemap/
    :alt: License

.. |CodeClimate| image:: https://codeclimate.com/github/nephila/djangocms-page-sitemap/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-page-sitemap
   :alt: Code Climate

======================
djangocms-page-sitemap
======================

|Gitter| |PyPiVersion| |PyVersion| |Status| |TestCoverage| |CodeClimate| |License|

django CMS page extension to handle sitemap customization

Support Python version:

* Python 2.7, 3.5, 3.6, 3.7

Supported Django versions:

* Django 1.11 to 2.2

Supported django CMS versions:

* django CMS 3.6+

.. note:: djangocms-page-sitemap 0.8 has been relicensed with BSD license.

.. note:: djangocms-page-sitemap 0.7 dropped compatibility with django CMS < 3.6. 0.6.x releases will be made if necessary after 0.6 release.


********
Features
********

* Support for changefreq and priority customisation per-page
* Option to exclude a page from the Sitemap
* Values are cached
* django CMS toolbar integration
* Available on Divio Cloud


**********
Quickstart
**********

* Install djangocms-page-sitemap::

    pip install djangocms-page-sitemap

* Add to ``INSTALLED_APPS`` with ``django.contrib.sitemaps``:

  .. code-block:: python

        INSTALLED_APPS = [
            ...
            "django.contrib.sitemaps",
            "djangocms_page_sitemap",
        ]

* Load it into the urlconf, eventually removing django CMS sitemap:

  .. code-block:: python

        ...
        urlpatterns = [
            path("admin/", admin.site.urls),
            ...
            path("", include("djangocms_page_sitemap.sitemap_urls")),
            ...
        ]

* Load ``robots_index`` templatetag and add it to the page in the head tag of the django CMS pages (or in a shared base template):

  .. code-block:: html+django

        {% load robots_index %}

        ...
        <head>
        <!-- somewhere in the head tag -->
        {% page_robots %}
        </head>
         ...

* If you need to provide a custom sitemap configuration (for example to add more
  sitemap classes to it, you can append the sitemap url explicitly:

  .. code-block:: python

        from django.contrib.sitemaps.views import sitemap
        from djangocms_page_sitemap.sitemap import ExtendedSitemap
        from myapp.sitemaps import MySiteSitemap

        urlpatterns = [
            ...
            path("sitemap.xml", sitemap, {
                "sitemaps": {
                    "cmspages": ExtendedSitemap, "myapp": MySiteSitemap,
                }
            ),
            ...
        ]


**************************
django-app-enabler support
**************************

`django-app-enabler`_ is supported.

You can either

* Installation & configuration: ``python -mapp_enabler install djangocms-page-meta``
* Autoconfiguration: ``python -mapp_enabler enable djangocms_page_meta``

Fully using this package will require some changes that cannot be modified by ``django-app-enabler``:

* Remove any existing sitemap declaration from ``urls.py``;
* Load robots tags in the page like outlined above;
* Run migrations: ``python manage.py migrate``

Check documentation above for details.

**********
Usage
**********

After installing as above, you will be able to tune the sitemap setting for each page.

A new menu item ``Sitemap properties`` will be available in the page toolbar.

For each page you will be able to set the following flags / values:

* Sitemap changefreq (default: the django CMS default)
* Sitemap priority (default: 0.5)
* Include page in sitemap (default: ``True``)
* Set ``noindex`` value to page robots meta tag
* Set ``noarchive`` value to page robots meta tag
* Provide any additional robots meta tag values

page_robots options
===================

``page_robots`` meta tag accepts the following parameters:

* ``page``: the page to render robots meta tag (default: current page). Can be
  any valid `page lookup`_
* ``site``: the current site id (default: current site).

Settings
===================

* PAGE_SITEMAP_CHANGEFREQ_LIST: List of frequency changes
* PAGE_SITEMAP_DEFAULT_CHANGEFREQ: Default changefrequency (default: django CMS value -monthly-)
* PAGE_SITEMAP_CACHE_DURATION: Cache duration: same as django CMS menu cache)


.. _page lookup: https://docs.django-cms.org/en/reference/templatetags.html#page_lookup
.. _django-app-enabler: https://github.com/nephila/django-app-enabler


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

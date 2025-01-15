.. :changelog:

*******
History
*******

.. towncrier release notes start

1.4.0 (2025-01-15)
==================

Features
--------

- Switch to Coveralls Github action (#104)
- Drop support for Django < 4.2, python < 3.10 and django CMS < 3.11 (#121)


Bugfixes
--------

- Do not double-check permissions (#123)


1.3.0 (2023-09-26)
==================

Features
--------

- Migrate to bump-my-version (#96)


1.2.0 (2023-05-08)
==================

Features
--------

- Update GH actions / linting configuration (#79)
- Add support for Django 4.2 / django CMS 3.11


1.1.0 (2022-08-27)
==================

Bugfixes
--------

- Fix error when populating the toolbar on page types (#67)
- Fixed serialization issue when trying to upload the addon to Divio Cloud. (#73)
- Add support for Django 3.2 / django CMS 3.10 (#74)


1.0.0 (2020-12-21)
==================

Features
--------

- Add support for django-app-enabler (#63)
- Update tooling and drop Python 2 / Django < 2.2 compatibility (#10208)

0.8.1 (2020-05-02)
==================

* Enable django CMS 3.7.2 on python 3

0.8.0 (2020-01-12)
==================

* Relicense under BSD license

0.7.0 (2019-08-22)
==================

* Add compatibility with Django 2.2
* Drop compatibility with Django < 1.11
* Drop compatibility with django CMS < 3.6
* Move to django-app-helper

0.6.0 (2019-07-13)
==================

* Drop compatibility with Django < 1.11
* Drop compatibility with Python 3 < 3.5

0.5.4 (2019-07-13)
==================

* Fix error when page_robots is executed outside a request
* Fix tox for older environments

0.5.3 (2019-03-09)
==================

* Add Django 2.0, 2.1 support
* Add django CMS 3.6 support
* Apply workaround to avoid triggering ``Page.site_id`` deprecation warning

0.5.2 (2018-04-07)
==================

* Make robots_extra not required

0.5.1 (2018-02-27)
==================

* Fix error in migration dependencies

0.5.0 (2018-02-22)
==================

* Add Django 1.11 support
* Add django CMS 3.5 support
* Package as Divio Cloud addon
* Add support for noindex, noarchive robots meta tag

0.4.3 (2019-07-13)
==================

* Fix error when page_robots is executed outside a request
* Fix tox for older environments

0.4.2 (2019-04-08)
==================

* Add support for noindex, noarchive robots meta tag

0.4.1 (2016-12-02)
==================

* Add Django 1.10 support

0.4.0 (2016-10-26)
==================

* Drop compatibility with django CMS 3.1 and below, Django 1.7 and below

0.3.1 (2015-10-18)
==================

* Improve defaults

0.3.0 (2015-10-18)
==================

* Add Python 3.5
* Add option to exclude page from sitemap

0.2.0 (2015-08-15)
==================

* Update to support django CMS 3.1
* Drop support for Django 1.4, 1.5
* Add support for Django 1.8

0.1.0 (2014-08-26)
==================

* Initial version.

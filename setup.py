#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_page_sitemap

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_page_sitemap.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-page-sitemap',
    version=version,
    description="""django CMS page extension to handle sitemap customization""",
    long_description=readme + '\n\n' + history,
    author='Iacopo Spalletti',
    author_email='i.spalletti@nephila.it',
    url='https://github.com/nephila/djangocms-page-sitemap',
    packages=[
        'djangocms_page_sitemap',
    ],
    include_package_data=True,
    install_requires=[
        'django-cms>3',
    ],
    license='GPLv2+',
    zip_safe=False,
    keywords='djangocms-page-sitemap',
    test_suite='cms_helper.run',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: English',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

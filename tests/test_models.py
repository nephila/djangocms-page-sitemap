from django import template
from django.contrib.auth.models import AnonymousUser
from django.contrib.sites.models import Site
from django.test import RequestFactory

from djangocms_page_sitemap.models import PageSitemapProperties

from .base import BaseTest


class RobotsTest(BaseTest):

    def _test_robots_tag(self, template_string, context, expected):

        tpl_obj = template.Template(template_string)
        ctx_obj = template.Context(context)
        rendered = tpl_obj.render(ctx_obj)
        self.assertEqual(rendered, expected)
        for key, value in context.items():
            self.assertEqual(ctx_obj.get(key), value)

    def test_robots_tag_no_request(self):
        template = '{% load robots_index %}{% page_robots %}'
        context = {}
        self._test_robots_tag(template, context, '')

    def test_robots_tag_request_no_page(self):
        template = '{% load robots_index %}{% page_robots %}'
        request = RequestFactory().get('/')
        request.session = {}
        context = {'request': request}
        self._test_robots_tag(template, context, '')

    def test_robots_options(self):
        page1, page2, page3 = self.get_pages()
        extension = PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never'
        )

        template = '{% load robots_index %}{% page_robots %}'
        expected = '<meta name="robots" content="">'
        context = {'request': self.get_page_request(page1, AnonymousUser())}
        self._test_robots_tag(template, context, expected)

        extension.noindex = True
        extension.save()
        expected = '<meta name="robots" content="noindex">'
        self._test_robots_tag(template, context, expected)

        extension.noarchive = True
        extension.save()
        expected = '<meta name="robots" content="noindex,noarchive">'
        self._test_robots_tag(template, context, expected)

        extension.robots_extra = 'nodmoz'
        extension.save()
        expected = '<meta name="robots" content="noindex,noarchive,nodmoz">'
        self._test_robots_tag(template, context, expected)

    def test_robots_page_parameter(self):
        page1, page2, page3 = self.get_pages()
        extension = PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never'
        )
        extension.refresh_from_db()

        template = '{% load robots_index %}{% page_robots %}'
        expected = ''
        context = {'request': self.get_page_request(page2, AnonymousUser())}
        self._test_robots_tag(template, context, expected)

        extension.noindex = True
        extension.save()
        expected = ''
        self._test_robots_tag(template, context, expected)

        template = '{%% load robots_index %%}{%% page_robots %s %%}' % page1.pk
        expected = '<meta name="robots" content="noindex">'
        self._test_robots_tag(template, context, expected)

        extension.noarchive = True
        extension.save()
        expected = '<meta name="robots" content="noindex,noarchive">'
        self._test_robots_tag(template, context, expected)

        extension.robots_extra = 'nodmoz'
        extension.save()
        expected = '<meta name="robots" content="noindex,noarchive,nodmoz">'
        self._test_robots_tag(template, context, expected)

    def test_robots_page_no_site(self):
        page1, page2, page3 = self.get_pages()
        extension = PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never'
        )
        extension.refresh_from_db()

        template = '{% load robots_index %}{% page_robots None "abc" %}'
        expected = ''
        context = {'request': self.get_page_request(page2, AnonymousUser())}
        self._test_robots_tag(template, context, expected)

    def test_robots_page_no_page(self):
        page1, page2, page3 = self.get_pages()
        extension = PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never'
        )
        extension.refresh_from_db()

        template = '{% load robots_index %}{% page_robots "abc" %}'
        expected = ''
        context = {'request': self.get_page_request(page2, AnonymousUser())}
        self._test_robots_tag(template, context, expected)

    def test_robots_page_other_site(self):
        site_2 = Site.objects.create(domain='http://othersite.com')
        page1, page2, page3 = self.get_pages()
        extension = PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never'
        )
        extension.refresh_from_db()

        template = '{%% load robots_index %%}{%% page_robots None %s %%}' % site_2.pk
        expected = ''
        context = {'request': self.get_page_request(page2, AnonymousUser())}
        self._test_robots_tag(template, context, expected)

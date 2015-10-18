# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.toolbar.items import Menu, ModalItem
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.test.utils import override_settings
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from djangocms_page_sitemap.cms_toolbar import PAGE_SITEMAP_MENU_TITLE
from djangocms_page_sitemap.models import PageSitemapProperties

from .base import BaseTest


class ToolbarTest(BaseTest):

    def test_no_page(self):
        """
        Test that no page menu is present if request not in a page
        """
        from cms.toolbar.toolbar import CMSToolbar
        request = self.get_page_request(None, self.user, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name='Page')
        self.assertEqual(page_menu, [])

    def test_no_perm(self):
        """
        Test that no page menu is present if user has no perm
        """
        from cms.toolbar.toolbar import CMSToolbar
        page1, page2, page3 = self.get_pages()
        request = self.get_page_request(page1, self.user_staff, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name='Page')
        self.assertEqual(page_menu, [])

    def test_perm(self):
        """
        Test that page meta menu is present if user has Page.change_perm
        """
        from cms.toolbar.toolbar import CMSToolbar
        page1, page2, page3 = self.get_pages()
        self.user_staff.user_permissions.add(Permission.objects.get(codename='change_page'))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus['page']
        self.assertEqual(len(page_menu.find_items(ModalItem, name="%s ..." % force_text(PAGE_SITEMAP_MENU_TITLE))), 1)

    @override_settings(CMS_PERMISSION=True)
    def test_perm_permissions(self):
        """
        Test that no page menu is present if user has general page Page.change_perm  but not permission on current page
        """
        from cms.toolbar.toolbar import CMSToolbar
        page1, page2, page3 = self.get_pages()
        self.user_staff.user_permissions.add(Permission.objects.get(codename='change_page'))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name='Page')
        self.assertEqual(page_menu, [])

    def test_toolbar(self):
        """
        Test that PageSitemapProperties item is present for superuser
        """
        from cms.toolbar.toolbar import CMSToolbar
        page1, page2, page3 = self.get_pages()
        request = self.get_page_request(page1, self.user, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus['page']
        self.assertEqual(len(page_menu.find_items(ModalItem, name="%s ..." % force_text(PAGE_SITEMAP_MENU_TITLE))), 1)

    def test_toolbar_with_items(self):
        """
        Test that PageSitemapProperties item is present for superuser if PageSitemapProperties exists for current page
        """
        from cms.toolbar.toolbar import CMSToolbar
        page1, page2, page3 = self.get_pages()
        page_ext = PageSitemapProperties.objects.create(
            extended_object=page1, priority='0.2', changefreq='never')
        request = self.get_page_request(page1, self.user, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus['page']
        meta_menu = page_menu.find_items(ModalItem, name="%s ..." % force_text(PAGE_SITEMAP_MENU_TITLE))[0].item
        self.assertTrue(meta_menu.url.startswith(reverse('admin:djangocms_page_sitemap_pagesitemapproperties_change', args=(page_ext.pk,))))
        self.assertEqual(force_text(page_ext), force_text(_('Sitemap values for Page %s') % page1.pk))

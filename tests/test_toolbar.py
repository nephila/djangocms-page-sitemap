from unittest import skipIf

import cms
from cms.api import create_page
from cms.test_utils.testcases import CMSTestCase
from cms.toolbar.items import Menu, ModalItem
from django.contrib.auth.models import Permission, User
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from djangocms_page_sitemap.cms_toolbars import PAGE_SITEMAP_MENU_TITLE
from djangocms_page_sitemap.models import PageSitemapProperties
from djangocms_page_sitemap.utils import is_versioning_enabled

from .base import BaseTest


def find_toolbar_buttons(button_name, toolbar):
    """
    Taken from: from djangocms_versioning.test_utils.test_helpers import find_toolbar_buttons

    CAVEAT: This test helper is not currently accesible due to the fact that it would then enforce
    versioning test packages and factory boy on this test suite.
    """
    found = []
    for button_list in toolbar.get_right_items():
        found = found + [button for button in button_list.buttons if button.name == button_name]
    return found


class ToolbarTest(BaseTest):
    def test_no_page(self):
        """
        Test that no page menu is present if request not in a page
        """
        from cms.toolbar.toolbar import CMSToolbar

        request = self.get_page_request(None, self.user, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        self.assertEqual(page_menu, [])

    def test_no_perm(self):
        """
        Test that no page menu is present if user has no perm
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, page2, page3 = self.get_pages()
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")

        self.assertEqual(len(page_menu), 1)

    def test_page_types(self):
        """
        Test that page meta menu is not displayed on page types.
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, page2, page3 = self.get_pages()
        page1.is_page_type = True
        page1.save()
        self.user_staff.user_permissions.add(Permission.objects.get(codename="change_page"))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        try:
            self.assertEqual(
                len(page_menu.find_items(ModalItem, name="%s..." % force_str(PAGE_SITEMAP_MENU_TITLE))),
                0,
            )
        except AssertionError:
            self.assertEqual(
                len(page_menu.find_items(ModalItem, name="%s ..." % force_str(PAGE_SITEMAP_MENU_TITLE))),
                0,
            )

    def test_perm(self):
        """
        Test that page meta menu is present if user has Page.change_perm
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, page2, page3 = self.get_pages()
        self.user_staff.user_permissions.add(Permission.objects.get(codename="change_page"))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        try:
            self.assertEqual(
                len(page_menu.find_items(ModalItem, name="%s..." % force_str(PAGE_SITEMAP_MENU_TITLE))),
                1,
            )
        except AssertionError:
            self.assertEqual(
                len(page_menu.find_items(ModalItem, name="%s ..." % force_str(PAGE_SITEMAP_MENU_TITLE))),
                1,
            )

    @override_settings(CMS_PERMISSION=True)
    def test_perm_permissions(self):
        """
        Test that no page menu is present if user has general page Page.change_perm  but not permission on current page
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, page2, page3 = self.get_pages()
        self.user_staff.user_permissions.add(Permission.objects.get(codename="change_page"))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        self.assertEqual(len(page_menu), 1)

    def test_toolbar(self):
        """
        Test that PageSitemapProperties item is present for superuser
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, page2, page3 = self.get_pages()
        request = self.get_page_request(page1, self.user, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        try:
            self.assertEqual(
                len(page_menu.find_items(ModalItem, name="%s..." % force_str(PAGE_SITEMAP_MENU_TITLE))),
                1,
            )
        except AssertionError:
            self.assertEqual(
                len(page_menu.find_items(ModalItem, name="%s ..." % force_str(PAGE_SITEMAP_MENU_TITLE))),
                1,
            )

    def test_toolbar_with_items(self):
        """
        Test that PageSitemapProperties item is present for superuser if PageSitemapProperties exists for current page
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, page2, page3 = self.get_pages()
        page_ext = PageSitemapProperties.objects.create(extended_object=page1, priority="0.2", changefreq="never")
        request = self.get_page_request(page1, self.user, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        try:
            meta_menu = page_menu.find_items(ModalItem, name="%s..." % force_str(PAGE_SITEMAP_MENU_TITLE))[0].item
        except IndexError:
            meta_menu = page_menu.find_items(ModalItem, name="%s ..." % force_str(PAGE_SITEMAP_MENU_TITLE))[0].item
        self.assertTrue(
            meta_menu.url.startswith(
                reverse("admin:djangocms_page_sitemap_pagesitemapproperties_change", args=(page_ext.pk,))
            )
        )
        self.assertEqual(force_str(page_ext), force_str(_("Sitemap values for Page %s") % page1.pk))


class VersioningToolbarTest(CMSTestCase):
    @skipIf(cms.__version__ < "4.0", "Versioning not available if django CMS < 4")
    def test_toolbar_buttons_are_not_duplicated(self):
        """
        The toolbar for djangocms-page-sitemap doesn't affect the toolbar buttons.

        This test Can be ran with or without versioning and should return the same result!
        """
        from cms.models import PageContent
        from cms.toolbar.utils import get_object_preview_url

        user = self.get_superuser()
        page_1 = create_page("page-one", "page.html", language="en", created_by=user)
        page_content = PageContent._base_manager.get(page=page_1, language="en")

        if is_versioning_enabled():
            page_content.versions.first().publish(user)
        preview_endpoint = get_object_preview_url(page_content, language="en")

        with self.login_user_context(self.get_superuser()):
            response = self.client.post(preview_endpoint)

        edit_button_list = find_toolbar_buttons("Edit", response.wsgi_request.toolbar)
        new_draft_button_list = find_toolbar_buttons("New Draft", response.wsgi_request.toolbar)
        create_button_list = find_toolbar_buttons("Create", response.wsgi_request.toolbar)

        self.assertEqual(len(create_button_list), 1)
        if is_versioning_enabled():
            self.assertEqual(len(new_draft_button_list), 1)
        else:
            self.assertEqual(len(edit_button_list), 1)

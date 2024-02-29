from cms.toolbar_pool import toolbar_pool
from cms.utils.conf import get_cms_setting
from cms.utils.permissions import has_page_permission
from django.urls import NoReverseMatch, reverse
from django.utils.translation import gettext_lazy as _

from .models import PageSitemapProperties

# Handle versioned toolbar if it exists, otherwise just use the normal CMS toolbar
try:
    from djangocms_versioning.cms_toolbars import VersioningPageToolbar as PageToolbar
except ImportError:
    from cms.cms_toolbars import PageToolbar


PAGE_SITEMAP_MENU_TITLE = _("Sitemap properties")


@toolbar_pool.register
class PageSitemapPropertiesMeta(PageToolbar):
    def populate(self):
        self.page = self.request.current_page
        if not self.page:
            return
        if self.page.is_page_type:
            # we don't need this on page types
            return

        # check global permissions if CMS_PERMISSIONS is active
        if get_cms_setting("PERMISSION"):
            has_global_current_page_change_permission = has_page_permission(
                self.request.user, self.request.current_page, "change"
            )
        else:
            has_global_current_page_change_permission = False
        # check if user has page edit permission
        can_change = self.request.current_page and self.request.current_page.has_change_permission(self.request.user)
        if has_global_current_page_change_permission or can_change:
            not_edit_mode = not self.toolbar.edit_mode_active
            current_page_menu = self.toolbar.get_or_create_menu("page")
            # Page tags
            try:
                page_extension = PageSitemapProperties.objects.get(extended_object_id=self.page.pk)
            except PageSitemapProperties.DoesNotExist:
                page_extension = None
            try:
                if page_extension:
                    url = reverse(
                        "admin:djangocms_page_sitemap_pagesitemapproperties_change", args=(page_extension.pk,)
                    )
                else:
                    url = "{}?extended_object={}".format(
                        reverse("admin:djangocms_page_sitemap_pagesitemapproperties_add"), self.page.pk
                    )
            except NoReverseMatch:  # pragma: no cover
                # not in urls
                pass
            else:
                current_page_menu.add_modal_item(PAGE_SITEMAP_MENU_TITLE, url=url, disabled=not_edit_mode)

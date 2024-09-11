from cms.api import get_page_draft
from cms.cms_toolbars import PAGE_MENU_THIRD_BREAK
from cms.toolbar.items import Break
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.urls import NoReverseMatch, reverse
from django.utils.translation import gettext_lazy as _

from .models import PageSitemapProperties

PAGE_SITEMAP_MENU_TITLE = _("Sitemap properties")


@toolbar_pool.register
class PageSitemapPropertiesMeta(CMSToolbar):
    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)
        if not self.page:
            return
        if self.page.is_page_type:
            # we don't need this on page types
            return

        # check if user has page change permission (respects CMS_PERMISSION)
        can_change = self.request.current_page and self.request.current_page.has_change_permission(self.request.user)
        if can_change:
            not_edit_mode = not self.toolbar.edit_mode_active
            current_page_menu = self.toolbar.get_or_create_menu("page")
            position = current_page_menu.find_first(Break, identifier=PAGE_MENU_THIRD_BREAK) - 1
            # Page tags
            try:
                page_extension = PageSitemapProperties.objects.get(extended_object_id=self.page.pk)
            except PageSitemapProperties.DoesNotExist:
                page_extension = None
            try:
                if page_extension:
                    url = reverse(
                        "admin:djangocms_page_sitemap_pagesitemapproperties_change",
                        args=(page_extension.pk,),
                    )
                else:
                    url = "{}?extended_object={}".format(
                        reverse("admin:djangocms_page_sitemap_pagesitemapproperties_add"),
                        self.page.pk,
                    )
            except NoReverseMatch:  # pragma: no cover
                # not in urls
                pass
            else:
                current_page_menu.add_modal_item(
                    PAGE_SITEMAP_MENU_TITLE,
                    url=url,
                    disabled=not_edit_mode,
                    position=position,
                )

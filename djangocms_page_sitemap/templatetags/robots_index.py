from classytags.arguments import Argument
from classytags.core import Options, Tag
from cms.templatetags.cms_tags import _get_page_by_untyped_arg
from django import template
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.tag(name='page_robots')
class PageRobots(Tag):
    """
    Generates the robots meta tag according to the extension attributes
    """
    name = 'page_robots'
    options = Options(
        Argument('page', required=False),
        Argument('site_id', required=False),
    )

    def render_tag(self, context, page, site_id):
        request = context.get('request')
        if not request:
            return ''
        if not site_id:
            site_id = get_current_site(request).pk
        if not page:
            try:
                page = request.current_page
            except AttributeError:
                pass
        else:
            page = _get_page_by_untyped_arg(page, request, site_id)
        content = []
        if not page:
            return ''
        try:
            if page.pagesitemapproperties.noindex:
                content.append('noindex')
            if page.pagesitemapproperties.noarchive:
                content.append('noarchive')
            if page.pagesitemapproperties.robots_extra:
                content.append(page.pagesitemapproperties.robots_extra)
            return '<meta name="robots" content="%s">' % ','.join(content)
        except ObjectDoesNotExist:
            return ''

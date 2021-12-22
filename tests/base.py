from io import StringIO

from cms.models import PageContent
from cms.utils.i18n import get_language_list
from django.contrib.auth.models import User
from django.http import SimpleCookie
from django.test import RequestFactory, TestCase

from djangocms_page_sitemap.utils import is_versioning_enabled


class BaseTest(TestCase):
    """
    Base class with utility function
    """
    request_factory = None
    user = None
    languages = get_language_list()
    page_data = {
        'changefreq': 'never',
        'priority': '0.3',
    }

    @classmethod
    def setUpClass(cls):
        cls.request_factory = RequestFactory()
        cls.user = User.objects.create(username='admin', is_staff=True, is_superuser=True)
        cls.user_staff = User.objects.create(username='staff', is_staff=True)
        cls.user_normal = User.objects.create(username='normal')

    def get_pages(self):
        from cms.api import create_page, create_title
        page_1 = create_page('page one', 'page.html', language='en', created_by=self.user)
        page_2 = create_page('page two', 'page.html', language='en', created_by=self.user)
        page_3 = create_page('page three', 'page.html', language='en', created_by=self.user)
        page_1_content_fr = create_title(language='fr', title='page un', page=page_1, created_by=self.user)
        page_1_content_it = create_title(language='it', title='pagina uno', page=page_1, created_by=self.user)
        page_3_content_fr = create_title(language='fr', title='page trois', page=page_3, created_by=self.user)
        page_content1 = PageContent._original_manager.get(page=page_1, language="en")
        page_content2 = PageContent._original_manager.get(page=page_2, language="en")
        page_content3 = PageContent._original_manager.get(page=page_3, language="en")
        if is_versioning_enabled():
            page_content1.versions.first().publish(self.user)
            page_content2.versions.first().publish(self.user)
            page_content3.versions.first().publish(self.user)
            page_1_content_fr.versions.first().publish(self.user)
            page_1_content_it.versions.first().publish(self.user)
            page_3_content_fr.versions.first().publish(self.user)
        if hasattr(page_1, 'set_as_homepage'):
            page_1.set_as_homepage()

        return page_1, page_2, page_3

    def get_request(self, page, lang):
        request = self.request_factory.get(page.get_path(lang))
        request.current_page = page
        request.user = self.user
        request.session = {}
        request.cookies = SimpleCookie()
        request.errors = StringIO()
        request.LANGUAGE_CODE = lang
        return request

    def get_page_request(self, page, user, path=None, edit=False, lang_code='en'):
        from cms.middleware.toolbar import ToolbarMiddleware
        path = path or page and page.get_absolute_url(lang_code)
        if edit:
            path += '?edit'
        request = RequestFactory().get(path)
        request.session = {}
        request.user = user
        request.LANGUAGE_CODE = lang_code
        if edit:
            request.GET = {'edit': None}
        else:
            request.GET = {'edit_off': None}
        request.current_page = page
        mid = ToolbarMiddleware(request)
        mid.process_request(request)
        return request

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()

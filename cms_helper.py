# -*- coding: utf-8 -*-
gettext = lambda s: s

HELPER_SETTINGS = {
        'NOSE_ARGS':['-s'],
        'ROOT_URLCONF':'tests.test_utils.urls',
        'INSTALLED_APPS':[
            'django.contrib.sitemaps',
        ],
        'LANGUAGE_CODE':'en',
        'LANGUAGES':(
            ('en', gettext('English')),
            ('fr', gettext('French')),
            ('it', gettext('Italiano')),
        ),
        'CMS_LANGUAGES':{
            1: [
                {
                    'code': 'en',
                    'name': gettext('English'),
                    'public': True,
                },
                {
                    'code': 'it',
                    'name': gettext('Italiano'),
                    'public': True,
                },
                {
                    'code': 'fr',
                    'name': gettext('French'),
                    'public': True,
                },
            ],
            'default': {
                'hide_untranslated': False,
            },
        },

}
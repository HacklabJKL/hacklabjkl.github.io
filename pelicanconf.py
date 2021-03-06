#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hacklab Jyv\xe4skyl\xe4 ry'
SITENAME = u'HacklabJKL'
SITETITLE = SITENAME
SITEURL = 'http://localhost:8000'
THEME = 'Flex'

FAVICON = SITEURL + '/images/favicon.ico'

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'
LOCALE = ('fi_FI.UTF-8', 'fi_FI', 'fi')

DEFAULT_LANG = u'fi'

STATIC_PATHS = ['images', 'blogimg', 'pdfs', 'extra/CNAME']

I18N_SUBSITES = {
    'en': {
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': 'Flex_en',
        'THEME_STATIC_DIR': '../theme'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ('hacklab.fi', 'http://hacklab.fi/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
    ('irc:  #hacklab.jkl @freenode', 'http://webchat.freenode.net/?channels=%23hacklab.jkl&uio=MTY9dHJ1ZSYxMT0yNDY57'),
    ('<iframe style="margin-top: 2em;" frameBorder="0" width="200" height="200" src="http://hacklab.ihme.org/visitors/api/v1/visitors?format=iframe"> </iframe>', ''),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = [
    # ...
    'pelican_vimeo',
    'i18n_subsites'
    # ...
]

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

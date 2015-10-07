#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hacklab Jyv\xe4skyl\xe4 ry'
SITENAME = u'HacklabJKL'
SITEURL = ''
THEME = 'Flex'

FAVICON = SITEURL + '/images/favicon.ico'

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'
LOCALE = ('fi_FI', 'fi')

DEFAULT_LANG = u'fi'

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
    ('#hacklab.jkl @freenode', 'http://webchat.freenode.net/?channels=%23hacklab.jkl&uio=MTY9dHJ1ZSYxMT0yNDY57'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = [
    # ...
    'pelican_vimeo',
    # ...
]

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

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
LOCALE = ('fi_FI.UTF-8', 'fi_FI', 'fi')

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
    ('irc:  #hacklab.jkl @freenode', 'http://webchat.freenode.net/?channels=%23hacklab.jkl&uio=MTY9dHJ1ZSYxMT0yNDY57'),
#    ('<iframe style="margin-top: 2em;" frameBorder="0" width="200" src="http://koti.kapsi.fi/jpa/stuff/hacklab-wlan-users.html"> </iframe>', ''),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = [
    # ...
    'pelican_vimeo',
    # ...
]

STATIC_PATHS = ['images', 'blogimg', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
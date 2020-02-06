#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TMCG 412 Group 1'
SITENAME = 'Monster Hunter World : Iceborne Hunter Guide'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']


TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

THEME = "pure"
COVER_IMG_URL = "../images/Nergigante.png"
TAGLINE = "TCMG 412 Group 1"
DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True 

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
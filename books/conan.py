#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseComicBook

def getBook():
    return Conan

class Conan(BaseComicBook):
    title               = u'名侦探柯南'
    description         = u'日本漫画家青山刚昌创作的侦探漫画'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_comic.gif'
    coverfile           = 'cv_conan.jpg'
    mainurl             = 'http://www.cartoonmad.com/comic/1066.html'

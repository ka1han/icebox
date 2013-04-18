#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('icebox.upload',
    url(r'^up/$', 'upload', name='upload'),
)

urlpatterns += patterns(('icebox.views'),   
    url(r'^$', 'blog_list', name='bloglist'),
    url(r'^blog/tag/(?P<id>\d+)/$', 'blog_filter', name='filtrblog'),
    url(r'^blog/search/$', 'blog_search', name='searchblog'),
    url(r'^blog/(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    url(r'^blog/(?P<id>\w+)/del/$', 'blog_del', name='delblog'),
    url(r'^blog/(?P<id>\w+)/update/$', 'blog_update', name='updateblog'),
    url(r'^blog/add/$', 'blog_add', name='addblog'),
    url(r'^blog/addmassage/$', 'add_weibo', name='addmassage'),
    url(r'^blog/showweibo/$', 'show_weibo', name='showweibo'),
    url(r'^blog/(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='showcomment'),
)

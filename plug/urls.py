#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns(('plug'),   
    url(r'^xss/$', 'xss.xss'),
)

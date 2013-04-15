#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
jelly xss
接口
http://ice.box/plug/xss/?xss=
xss.js
http://ice.box/static/js/xss.js
'''

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
# from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from plug.models import *

def xss(request):
    if request.method == 'GET':
        cookie = request.GET['xss']
        s = Xss(cookie=cookie)
        s.save()
        return render_to_response("404.html")
    else:
        return render_to_response("404.html")

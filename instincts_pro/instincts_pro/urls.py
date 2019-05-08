"""instincts_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
##from django.contrib import admin
###from django.urls import path
##from django.conf.urls import include,url
##
##from django.conf.urls.defaults import *
###from django.contrib.urls import include,path
##
##urlpatterns = [
##    url(r'^instincts_app/',include('instincts_app.urls')),
##    url(r'^admin/', admin.site.urls),
##]
# helloworld_project/urls.py
##from django.contrib import admin
##from django.urls import path
##from django.urls import include
##from django.urls import path
##urlpatterns = [
##    path('admin/', admin.site.urls)
####    path('', include('instincts_app.urls')),
##]
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]



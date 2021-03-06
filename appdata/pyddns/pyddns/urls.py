"""pyddns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from common.views import *
from pyddns.views import *
import os


urlpatterns = [
    url(r'^main/(?P<id_user>.*)', main),
    url(r'^main/', main),
    url(r'^users/(?P<buscar>.*)', users),
    url(r'^users/', users),
    url(r'^domains/(?P<buscar>.*)', domains),
    url(r'^domains/', domains),
    url(r'^add_user/(?P<id_user>\d+)', add_user),
    url(r'^add_user/', add_user),
    url(r'^add_subdomain', add_subdomain),
    url(r'^set_user', set_user),
    url(r'^delet_user', delet_user),
    url(r'^delet_domain', delet_domain),
    url(r'^common/', include('common.urls')),
    url(r'^nic/update', updateip),
    url(r'^ip/update/(?P<domain>.*)/(?P<ip>.*)', set_ip_web),
    url(r'^$', main),
]

#Add admin url
admin_url='admin'
if os.environ.get('DJANGO_ADMIN_URL'):
    additional_settings = url(r'^'+ os.environ.get('DJANGO_ADMIN_URL') +"/", admin.site.urls),
else:
    additional_settings = url(r'^admin/', admin.site.urls),
urlpatterns += additional_settings
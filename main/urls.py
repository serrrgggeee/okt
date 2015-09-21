# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import Main,  MainDetailView


urlpatterns = patterns('',



    # Detail View
    url(r'^$', Main.as_view(), name='main'),
    url(r'^(?P<slug>[^/]+)/$', MainDetailView.as_view(), name='main'),
)

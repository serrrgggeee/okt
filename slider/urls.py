# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import SliderListView, SliderDetailView


urlpatterns = patterns('',

    # List View
    url(r'^$', SliderListView.as_view(), name="slidermember_list"),

    # Detail View
    url(r'^(?P<slug>[^/]+)/$', SliderDetailView.as_view(), name='slidermember_detail'),
)

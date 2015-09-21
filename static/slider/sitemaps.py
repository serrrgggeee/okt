# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from .models import SliderMember


class SliderSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.75

    def items(self):
        return SliderMember.objects.all()

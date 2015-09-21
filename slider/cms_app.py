# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .menu import SliderSubMenu


class SliderApp(CMSApp):
    name = _('Slider')
    urls = ['slider.urls', ]
    app_name = 'slider'
    menus = [SliderSubMenu, ]

apphook_pool.register(SliderApp)

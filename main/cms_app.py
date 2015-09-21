# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

#from .menu import StaffSubMenu


class MainApp(CMSApp):
    name = _('Main')
    urls = ['main.urls', ]
    app_name = 'main'
    #menus = [StaffSubMenu, ]

apphook_pool.register(MainApp)

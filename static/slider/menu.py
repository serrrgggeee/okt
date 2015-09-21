# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import SliderMember


class SliderSubMenu(CMSAttachMenu):

    name = _("Slider Sub-Menu")

    def get_nodes(self, request):
        nodes = []

        for slider in SliderMember.objects.order_by('full_name').all():

            node = NavigationNode(
                mark_safe(slider.full_name),
                slider.get_absolute_url(),
                slider.id,
            )

            nodes.append(node)

        return nodes

menu_pool.register_menu(SliderSubMenu)

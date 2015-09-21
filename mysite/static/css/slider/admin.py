# -*- coding: utf-8 -*-

from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from easy_select2 import select2_modelform
#from clippings.models import Clipping
from .models import Group, SliderMember


class GroupAdmin(admin.ModelAdmin):
	pass

admin.site.register(Group,GroupAdmin)


#class ClippingInline(SortableTabularInline):
#    extra = 1
#    form = select2_modelform(Clipping, attrs={'width': '250px'})
#    model = Clipping


class SliderMemberAdmin(PlaceholderAdminMixin, SortableAdmin):
	form = select2_modelform(SliderMember, attrs={'width': '250px'})
#	inlines = [ ClippingInline, ]

admin.site.register(SliderMember, SliderMemberAdmin)
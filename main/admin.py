# -*- coding: utf-8 -*-

from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from easy_select2 import select2_modelform
from clippings.models import Clipping
from .models import Main


class MainAdmin(admin.ModelAdmin):
	pass

admin.site.register(Main, MainAdmin)


class ClippingInline(SortableTabularInline):
    extra = 1
    form = select2_modelform(Clipping, attrs={'width': '250px'})
    model = Clipping



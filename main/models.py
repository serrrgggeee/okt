# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models

from adminsortable.models import Sortable
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField


class Main(Sortable):
    class Meta:
        app_label = 'main'

    full_name = models.CharField(
        u'full name',
        blank=False,
        default='',
        help_text=u'Please enter a full name for this main member',
        max_length=64,
        unique=True,
    )


    def get_absolute_url(self):
        return '/'
    photo = FilerImageField(
        blank=True,
        help_text=u'Optional. Please supply a photo of this main member.',
        null=True,
        on_delete=models.SET_NULL,  # Important
    )

    bio = PlaceholderField('main_bio')


    def __unicode__(self):
        return self.full_name

# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models

from adminsortable.models import Sortable
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from django_resized import ResizedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from sorl.thumbnail import get_thumbnail

class Group(models.Model):
    class Meta:
        app_label = 'slider'
        verbose_name_plural = 'seniorities'

    label = models.CharField(
        u'label',
        blank=False,
        default='',
        help_text=u'Please provide a label for this group',
        max_length=64,
        unique=True,
    )

    def __unicode__(self):
        return self.label


class SliderMember(Sortable):
    class Meta:
        app_label = 'slider'

    full_name = models.CharField(
        u'full name',
        blank=False,
        default='',
        help_text=u'Please enter a full name for this slider member',
        max_length=64,
        unique=True,
    )
    related_staff = models.ManyToManyField(
        'staff.StaffMember',
        blank=True,
        help_text=u'Optional. Please choose zero or more main related to '
                  u'this item. Selected  will automatically get a '
                  u'Clipping added that references this news item.',
        null=True,
        related_name='slider',
        verbose_name=u'related staff',
    )

    slug = models.SlugField(
        u'slug',
        blank=False,
        default='',
        help_text=u'Provide a unique slug for this slider member',
        max_length=64,
    )
    active = models.SlugField(
        u'active',
        blank=False,
        default='',
        help_text=u'Provide a unique active for this slider member',
        max_length=64,
    )

    group = models.ForeignKey(
        'slider.Group',
        blank=True,
        default=None,
        help_text=u'Please specify a group level for this slider member',
        null=True
    )

    #photo = FilerImageField(
    #    blank=True,
    #    help_text=u'Optional. Please supply a photo of this slider member.',
    #    null=True,
    #    on_delete=models.SET_NULL,  # Important
    #)
    image1			= models.ImageField(upload_to='photo', null=True,)
    photo_small =ImageSpecField([
			ResizeToFill(550, 550)], source='image1',
			options={'quality': 70})

    bio = PlaceholderField('slider_bio')

    def get_image_200x200(self):
        return get_thumbnail(self.photo, '200x200', crop='center')
    def get_absolute_url(self):
        return reverse('slider:slidermember_detail', kwargs={'slug': self.slug, })

    def __unicode__(self):
        return self.full_name

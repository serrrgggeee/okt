# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView

from .models import SliderMember


class SliderListView(ListView):
    model = SliderMember
    queryset = SliderMember.objects.order_by('order').all()

    #def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
    #    if self.request.toolbar and self.request.toolbar.edit_mode:
    #        menu = self.request.toolbar.get_or_create_menu('slider-list-menu', 'Leadership')
     #       menu.add_sideframe_item(u'Seniority List', url=reverse('admin:slider_seniority_changelist'))
     #       menu.add_modal_item('Add new Seniority', url="%s" % (reverse('admin:slider_seniority_add'), ))
     #       menu.add_break()
     #       menu.add_sideframe_item(u'Slider List', url=reverse('admin:slider_slidermember_changelist'))
     #       menu.add_modal_item('Add new slider Member', url="%s" % (reverse('admin:slider_slidermember_add'), ))

     #   return super(SliderListView, self).render_to_response(context, **response_kwargs)


class SliderDetailView(DetailView):
    model = SliderMember
    context_object_name = 'slider'

    #def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        #if self.request.toolbar and self.request.toolbar.edit_mode:
           # menu = self.request.toolbar.get_or_create_menu('slider-member-menu', self.object.full_name)
           # menu.add_modal_item('Edit %s' % self.object.full_name, url=reverse('admin:slider_slidermember_change', args=[self.object.id]), )

            #menu.add_break()

            # Ho hum...
            #menu.add_modal_item('Attach New Clipping',
            #     url="%s" % (reverse('admin:clippings_clipping_add'), )
            #)

            # Coolness...
            #menu.add_modal_item('Attach New Clipping',
            #    url="%s?slider=%d" % (
            #        reverse('admin:clippings_clipping_add'),
            #        self.object.id,
            #    )
            #)


        #return super(SliderDetailView, self).render_to_response(context, **response_kwargs)

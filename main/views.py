# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView

from .models import Main


#class StaffListView(ListView)
class MainDetailView(DetailView):
    model = Main
    context_object_name = 'main'

class Main(ListView):
    model = Main
    queryset = Main.objects.order_by('order').all()
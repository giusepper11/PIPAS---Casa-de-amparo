from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class MapsTestView(TemplateView):
    template_name = 'new_features/maps_test.html'



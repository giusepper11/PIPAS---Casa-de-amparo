from django.shortcuts import render
from casa_amparo.doacoes.models import DemandaDoacao
from django.views.generic import ListView, DetailView


# Create your views here.

class DoacoesDetailView(DetailView):
    context_object_name = 'doacao'
    model = DemandaDoacao
    template_name = 'doacoes/offer_donation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from instituicoes.models import InstituicaoLista


# Create your views here.


class InstituicoesListView(ListView):
    model = InstituicaoLista
    template_name = 'instituicoes/lista_inst.html'

    def get_queryset(self):
        return self.model.objects.exclude(instituicao__isnull=True).exclude(instituicao__exact='').order_by('bairro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bairros'] = InstituicaoLista.objects.order_by().values('bairro').distinct()
        return context



class BairrosListView(TemplateView):
    template_name = 'instituicoes/lista_inst.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bairros'] = InstituicaoLista.objects.order_by().values('bairro').distinct()
        return context

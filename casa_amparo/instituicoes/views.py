import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.db.models import Q

from casa_amparo.instituicoes.models import InstituicaoLista


# Create your views here.


class InstituicoesListView(ListView):
    model = InstituicaoLista
    template_name = 'instituicoes/lista_inst.html'

    def get_queryset(self):
        return self.model.objects.exclude(instituicao__isnull=True).exclude(instituicao__exact='').exclude(
            editado=False).order_by('bairro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['bairros'] = InstituicaoLista.objects.order_by('bairro').values('bairro').distinct()
        context['bairros'] = self.get_queryset().order_by('bairro').values('bairro').distinct()
        context['body_style'] = 'ecommerce-page'
        return context


class InstituicaoDetailView(DetailView):
    model = InstituicaoLista
    template_name = 'instituicoes/detail_inst.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_style'] = 'profile-page'
        return context


@csrf_exempt
def ajax_instfilter(request):
    if request.method == 'POST':
        filtro = json.loads(request.body)
        if filtro:
            if filtro.get('bairro'):
                inst_filter = InstituicaoLista.objects.filter(bairro__in=filtro['bairro']).values('pk', 'instituicao',
                                                                                                  'endereco', 'bairro')
                json_posts = mark_safe(json.dumps(list(inst_filter), ensure_ascii=False))
                return HttpResponse(json_posts)

    inst_filter = InstituicaoLista.objects.exclude(instituicao__isnull=True).exclude(instituicao__exact='').order_by(
        'bairro').values('pk', 'instituicao', 'endereco', 'bairro')
    json_posts = mark_safe(json.dumps(list(inst_filter), ensure_ascii=False))
    return HttpResponse(json_posts)

# class BairrosListView(TemplateView):
#     template_name = 'instituicoes/lista_inst.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['bairros'] = InstituicaoLista.objects.order_by().values('bairro').distinct()
#         return context

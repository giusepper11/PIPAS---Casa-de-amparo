from django.urls import path, include
from instituicoes.views import InstituicoesListView, ajax_instfilter
from django.views.decorators.cache import never_cache


app_name = 'instituicoes'

urlpatterns = [
    path('', InstituicoesListView.as_view(), name='lista_bairros'),

    path('inst_filter/', ajax_instfilter, name='ajax_instfilter'),
]

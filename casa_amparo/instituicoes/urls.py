from django.urls import path

from casa_amparo.instituicoes.views import InstituicoesListView, InstituicaoDetailView, ajax_instfilter

app_name = 'instituicoes'

urlpatterns = [
    path('', InstituicoesListView.as_view(), name='lista_bairros'),
    path('<int:pk>', InstituicaoDetailView.as_view(), name='inst_detail'),

    path('inst_filter/', ajax_instfilter, name='ajax_instfilter'),
]

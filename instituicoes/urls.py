from django.urls import path, include
from instituicoes.views import InstituicoesListView
from django.views.decorators.cache import never_cache


app_name = 'instituicoes'

urlpatterns = [
    path('', never_cache(InstituicoesListView.as_view()), name='lista_bairros'),
]

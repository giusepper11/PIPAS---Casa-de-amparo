from django.urls import path, include
from casa_amparo.doacoes.views import DoacoesDetailView
from django.views.decorators.cache import never_cache

app_name = 'doacoes'

urlpatterns = [

    path('<int:pk>', DoacoesDetailView.as_view(), name='doacao_detail'),

]

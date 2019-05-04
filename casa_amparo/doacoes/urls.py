from django.urls import path

from casa_amparo.doacoes.views import DoacoesUpdatelView, DoacaoOutrosCreateView, DoacaoDashboardView, UserDonate

app_name = 'doacoes'

urlpatterns = [

    path('<int:pk>', DoacoesUpdatelView.as_view(), name='doacao_update'),
    path('<int:inst_pk>/create_other_donation/', DoacaoOutrosCreateView.as_view(), name='doacao_outros_create'),
    path('donation_dashboard/', DoacaoDashboardView.as_view(), name='doacao_dashboard'),
    path('<int:inst_pk>/offer_donation/<int:donation_pk>', UserDonate.as_view(), name='oferta_doacao'),

]

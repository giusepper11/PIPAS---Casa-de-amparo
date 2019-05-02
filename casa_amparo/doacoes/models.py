from django.db import models
from django.urls import reverse

from casa_amparo.instituicoes.models import InstituicaoLista
from casa_amparo.users.models import Pessoa, CustomUser


class DemandaDoacao(models.Model):
    instituicao = models.ForeignKey(InstituicaoLista, on_delete=models.DO_NOTHING)
    doacao = models.CharField(max_length=200)
    qtd = models.IntegerField(default=1)
    obs = models.TextField(blank=True, null=True)
    recebido = models.BooleanField(default=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.instituicao.instituicao} : {self.doacao}"


#
class DoacaoUser(models.Model):
    doador = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    demanda = models.ForeignKey(DemandaDoacao, on_delete=models.DO_NOTHING)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)
    obs = models.TextField(blank=True, null=True)


#

class DoacaoOutros(models.Model):
    TIPO_DOACAO = (
        ('MONEY', 'Dinheiro'),
        ('PRODUCTS', 'Produtos'),
        ('SERVICES', 'Serviços')
    )

    doador = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    instituicao = models.ForeignKey(InstituicaoLista, on_delete=models.DO_NOTHING)
    tipo_doacao = models.CharField(max_length=8, choices=TIPO_DOACAO)
    doacao = models.CharField(max_length=300)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doador.username} : {self.doacao}"

    def get_absolute_url(self):
        return reverse('home_page')

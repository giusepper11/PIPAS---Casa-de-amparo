from django.db import models
from users.models import Instituicoes
# Create your models here.


class InstituicaoLista(models.Model):
    id = models.IntegerField(primary_key=True)
    instituicao = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    entidade_que_administra_o_abrigo = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    idade = models.CharField(max_length=255, blank=True, null=True)
    numero_de_criancas = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=255, blank=True, null=True)
    possui_programa_de_apadrinhamento_afetivo = models.CharField(max_length=255, blank=True, null=True)
    responsavel = models.CharField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=255, blank=True, null=True)
    end_format = models.CharField(max_length=255, blank=True, null=True)
    lat_long = models.CharField(max_length=255, blank=True, null=True)
    user_inst = models.ForeignKey(Instituicoes, blank=True, null=True, on_delete=models.DO_NOTHING)
    logo_img = models.ImageField(blank=True, null=True)
    autorizado = models.BooleanField(default=False)
    editado = models.BooleanField(default=False)

    def __str__(self):
        try:
            return self.instituicao.capitalize()
        except:
            return 'instutição sem nome'

    def get_lat_long(self):
        if self.lat_long:
            long_lat = self.lat_long.split(',')
            return {'lng': long_lat[-1], 'lat': long_lat[0]}
        else:
            return None

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome + '-' + self.uf

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome + '-' + self.uf.uf

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    cep = models.CharField(max_length=8)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_manutencao = models.DateTimeField()
    controle = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    profile_pic = models.ImageField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11)


class PessoaJurica(Pessoa):
    cnpj = models.CharField(max_length=14)


class Instituicoes(models.Model):
    adm = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    pf = models.OneToOneField(PessoaJurica, on_delete=models.DO_NOTHING)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    def __str__(self):
        return self.pf.nome


class Mensagens(models.Model):
    mensagem = models.TextField(max_length=1000)
    data_msg = models.DateTimeField(auto_now_add=True)
    remetente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.remetente} - {self.destinatario}'

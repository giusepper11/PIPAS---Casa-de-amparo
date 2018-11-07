from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.uf


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome + '-' + self.uf.uf


class User(AbstractUser):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, blank=True, null=True)
    cep = models.CharField(max_length=8)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_manutencao = models.DateTimeField(blank=True, null=True)
    controle = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    profile_pic = models.ImageField(blank=True, null=True)
    is_pf = models.BooleanField(default=False)
    is_pj = models.BooleanField(default=False)

    def __str__(self):
        return f'Usuario :{self.username}'


class PessoaFisica(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, primary_key=True)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return f'Pessoa Fisica :{self.user.nome}'


class PessoaJuridica(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, primary_key=True)
    cnpj = models.CharField(max_length=14)
    is_instituicao = models.BooleanField(default=False)

    def __str__(self):
        return f'Pessoa Juridica :{self.user.nome}'


class Instituicoes(models.Model):
    pf = models.OneToOneField(PessoaJuridica, on_delete=models.DO_NOTHING, primary_key=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.pf.user.nome


class Mensagens(models.Model):
    mensagem = models.TextField(max_length=1000)
    data_msg = models.DateTimeField(auto_now_add=True)
    remetente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.remetente} - {self.destinatario}'


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

    class Meta:
        managed = True
        db_table = 'instituicao_lista'

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

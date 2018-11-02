from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.register(PessoaJurica)
admin.site.register(PessoaFisica)
admin.site.register(Instituicoes)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Mensagens)
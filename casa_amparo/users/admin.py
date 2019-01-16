from django.contrib import admin
from casa_amparo.users.models import *

#

admin.site.register(CustomUser)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Instituicoes)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Mensagens)

from django.contrib import admin
from accounts.models import *

#

admin.site.register(User)
admin.site.register(PessoaJurica)
admin.site.register(PessoaFisica)
admin.site.register(Instituicoes)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Mensagens)
from django.contrib import admin
from casa_amparo.users.models import *


#

class UsuarioListaAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'eh_pf', 'eh_pj', 'esta_ativo')
    search_fields = ('email', 'username')
    list_filter = ('is_pf', 'is_pj', 'is_active')

    def esta_ativo(self, obj):
        if obj.is_active:
            return True
        else:
            return False

    esta_ativo.short_description = 'Ativo'
    esta_ativo.boolean = True

    def eh_pf(self, obj):
        if obj.is_pf:
            return True
        else:
            return False

    eh_pf.short_description = 'Pessoa Fisica'
    eh_pf.boolean = True

    def eh_pj(self, obj):
        if obj.is_pj:
            return True
        else:
            return False

    eh_pj.short_description = 'Pessoa Juridica'
    eh_pj.boolean = True


admin.site.register(CustomUser, UsuarioListaAdmin)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Instituicoes)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Mensagens)

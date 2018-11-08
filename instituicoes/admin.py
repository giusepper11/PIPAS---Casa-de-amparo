from django.contrib import admin
from instituicoes.models import *


# Register your models here.

class InstituicaoListaAdmin(admin.ModelAdmin):
    list_display = (
        'instituicao', 'endereco', 'bairro', 'telefone', 'email', 'foi_editado', 'tem_logo', 'foi_autorizado')
    search_fields = ('id', 'instituicao', 'bairro')
    list_filter = ('editado', 'autorizado',)

    def tem_logo(self, obj):
        if obj.logo_img:
            return True
        else:
            return False

    tem_logo.short_description = 'Logo?'
    tem_logo.boolean = True

    def foi_autorizado(self, obj):
        if obj.autorizado:
            return True
        else:
            return False

    foi_autorizado.short_description = 'Autorizado?'
    foi_autorizado.boolean = True

    def foi_editado(self, obj):
        if obj.editado:
            return True
        else:
            return False

    foi_editado.short_description = 'Editado?'
    foi_editado.boolean = True


admin.site.register(InstituicaoLista, InstituicaoListaAdmin)

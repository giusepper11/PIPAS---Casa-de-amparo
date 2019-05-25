from django.contrib import admin
from casa_amparo.doacoes.models import DemandaDoacao, DoacaoUser, DoacaoOutros


class DoacaoOutrosListaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'tipo_doacao', 'doacao', 'get_instituicao')
    search_fields = ('nome', 'instituicao__instituicao')
    list_filter = ('tipo_doacao',)

    def get_instituicao(self, obj):
        return obj.instituicao.instituicao

    get_instituicao.short_description = 'Instituição'
    get_instituicao.admin_order_field = 'instituicao__instituicao'


admin.site.register(DemandaDoacao)
admin.site.register(DoacaoUser)
admin.site.register(DoacaoOutros, DoacaoOutrosListaAdmin)

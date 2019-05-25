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


class DemandaDoacaoListAdmin(admin.ModelAdmin):
    list_display = ('get_instituicao', 'doacao', 'qtd', 'obs', 'foi_recebido', 'dt_criacao')
    search_fields = ('instituicao__instituicao', 'doacao')
    list_filter = ('doacao', 'recebido')

    def get_instituicao(self, obj):
        return obj.instituicao.instituicao

    get_instituicao.short_description = 'Instituição'
    get_instituicao.admin_order_field = 'instituicao__instituicao'

    def foi_recebido(self, obj):
        if obj.recebido:
            return True
        else:
            return False

    foi_recebido.short_description = 'Recebido'
    foi_recebido.boolean = True


admin.site.register(DemandaDoacao, DemandaDoacaoListAdmin)
admin.site.register(DoacaoUser)
admin.site.register(DoacaoOutros, DoacaoOutrosListaAdmin)

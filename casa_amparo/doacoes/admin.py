from django.contrib import admin

from casa_amparo.doacoes.models import DemandaDoacao, DoacaoUser, DoacaoOutros
from casa_amparo.utils.utils import ExportCsvMixin


class DoacaoOutrosListaAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('id', 'nome', 'telefone', 'tipo_doacao', 'doacao', 'get_instituicao')
    search_fields = ('nome', 'instituicao__instituicao')
    list_filter = ('tipo_doacao',)
    actions = ['export_as_csv']

    def get_instituicao(self, obj):
        return obj.instituicao.instituicao

    get_instituicao.short_description = 'Instituição'
    get_instituicao.admin_order_field = 'instituicao__instituicao'


class DemandaDoacaoListAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('get_instituicao', 'doacao', 'qtd', 'obs', 'foi_recebido', 'dt_criacao')
    search_fields = ('instituicao__instituicao', 'doacao')
    list_filter = ('doacao', 'recebido')
    actions = ['export_as_csv']

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


class DoacaoUserListAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('get_doador', 'get_instituicao', 'get_doacao', 'dt_criacao',)
    actions = ['export_as_csv']

    def get_doador(self, obj):
        return obj.doador.username

    get_doador.short_description = 'Doador'

    def get_doacao(self, obj):
        return obj.demanda.doacao

    get_doacao.short_description = 'Demanda'

    def get_instituicao(self, obj):
        return obj.demanda.instituicao.instituicao

    get_instituicao.short_description = 'Instituição'
    get_instituicao.admin_order_field = 'instituicao__instituicao'


admin.site.register(DemandaDoacao, DemandaDoacaoListAdmin)
admin.site.register(DoacaoUser, DoacaoUserListAdmin)
admin.site.register(DoacaoOutros, DoacaoOutrosListaAdmin)

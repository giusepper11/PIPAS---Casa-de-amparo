from rest_framework import serializers
from casa_amparo.doacoes.models import DoacaoOutros


class DoacaoOutrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoacaoOutros
        fields = ('nome', 'telefone', 'instituicao', 'tipo_doacao', 'doacao',)
        filter_fields = ('instituicao')

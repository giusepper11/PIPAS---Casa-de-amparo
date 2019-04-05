from rest_framework.serializers import ModelSerializer
from casa_amparo.instituicoes.models import InstituicaoLista


class InstituicaoSerializer(ModelSerializer):
    class Meta:
        model = InstituicaoLista
        fields = (
            '__all__'
        )
        filter_fields = ('id')

from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from casa_amparo.instituicoes.models import InstituicaoLista
from .serializers import InstituicaoSerializer


class InstituicaoViewSet(ReadOnlyModelViewSet):
    """

    """
    queryset = InstituicaoLista.objects.exclude(instituicao__isnull=True).exclude(instituicao__exact='').exclude(editado=False).order_by('instituicao')
    serializer_class = InstituicaoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('instituicao', 'bairro', 'cep')

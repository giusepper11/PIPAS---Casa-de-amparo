from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from casa_amparo.doacoes.api.serializers import DoacaoOutrosSerializer
from casa_amparo.doacoes.models import DoacaoOutros


class DoacaoOutrosViewSet(ModelViewSet):
    queryset = DoacaoOutros.objects.all()
    serializer_class = DoacaoOutrosSerializer
    lookup_field = 'instituicao'

    def perform_create(self, serializer):
        serializer.save()

    def retrieve(self, request, *args, **kwargs):
        query = DoacaoOutros.objects.filter(instituicao=kwargs.get('instituicao'))
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return Response({"Filtre por alguma instituição"})

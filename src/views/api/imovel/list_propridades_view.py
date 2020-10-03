from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework import mixins, generics, viewsets
from domain.imovel.models import Propriedade
from domain.imovel.serializers import PropriedadeSerializer


class ListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Endpoint devolve as propriedades proximas de um ponto ordenados pela distancia. Requires ?lat={}&lon={}
    """
    serializer_class = PropriedadeSerializer

    def get_queryset(self):
        lat = self.request.query_params.get('lat', None)
        lon = self.request.query_params.get('lon', None)

        if not lat or not lon:
            raise ValueError('É necessarios os dois parametros lat = {} | lon = {}.'.format(repr(lat), repr(lon)))

        origin = Point(float(lat), float(lon), None, 4326)

        queryset = Propriedade.objects.annotate(distance=Distance('posicao', origin)).order_by('distance')

        return queryset



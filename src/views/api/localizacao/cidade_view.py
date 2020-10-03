from domain.localizacao.models import Cidade
from domain.localizacao.serializers import CidadeSerializer
from rest_framework import generics


class CidadeCreateViewSet(generics.ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class CidadeViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

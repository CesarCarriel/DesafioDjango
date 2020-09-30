from domain.localizacao.models import Regiao
from domain.localizacao.serializers import RegiaoSerializer
from rest_framework import generics


class RegiaoCreateViewSet(generics.ListCreateAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer


class RegiaoViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer

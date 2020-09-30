from rest_framework import serializers
from domain.localizacao.models import Cidade


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado', 'regiao', 'slug']

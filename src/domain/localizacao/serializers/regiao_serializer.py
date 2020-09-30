from rest_framework import serializers
from domain.localizacao.models import Regiao


class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = ['id', 'nome', 'estado', 'slug']

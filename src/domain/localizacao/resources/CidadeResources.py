from import_export import resources
from domain.localizacao.models import Cidade


class CidadeResources(resources.ModelResource):
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado', 'regiao']

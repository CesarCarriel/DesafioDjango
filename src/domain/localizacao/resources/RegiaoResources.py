from import_export import resources
from domain.localizacao.models import Regiao


class RegiaoResources(resources.ModelResource):
    class Meta:
        model = Regiao
        fields = ['id', 'nome', 'estado']

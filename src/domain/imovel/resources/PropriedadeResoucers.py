from import_export import resources
from domain.imovel.models import Propriedade


class PropriedadeResources(resources.ModelResource):
    class Meta:
        model = Propriedade
        fields = ['id', 'nome', 'valor', 'tipo', 'criado_em', 'modificado_em']

from import_export import resources
from domain.imovel.models import Tipo


class TipoResources(resources.ModelResource):
    class Meta:
        model = Tipo
        fields = ['id', 'nome', 'criado_em', 'modificado_em']

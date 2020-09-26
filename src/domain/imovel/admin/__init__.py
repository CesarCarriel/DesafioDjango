from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from domain.imovel.resources.PropriedadeResoucers import PropriedadeResources
from domain.imovel.resources.TipoResources import TipoResources

from domain.imovel.models import Tipo, Propriedade


class TipoAdmin(ImportExportModelAdmin):
    resource_class = TipoResources
    list_display = ['nome', 'criado_em', 'modificado_em']


class PropriedadeAdmin(ImportExportModelAdmin):
    resource_class = PropriedadeResources
    list_display = ['nome', 'valor', 'tipo', 'foto', 'criado_em', 'modificado_em']
    list_filter = ['tipo__nome']
    search_fields = ['nome']


admin.site.register(Tipo, TipoAdmin)
admin.site.register(Propriedade, PropriedadeAdmin)

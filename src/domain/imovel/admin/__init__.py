from django.contrib import admin
from domain.imovel.models import Tipo, Propriedade


class TipoAdmin(admin.ModelAdmin):
    list_display = ['nome']


class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'tipo', 'foto']
    list_filter = ['tipo__nome']
    search_fields = ['nome']


admin.site.register(Tipo, TipoAdmin)
admin.site.register(Propriedade, PropriedadeAdmin)

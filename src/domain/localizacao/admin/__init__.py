from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from domain.localizacao.resources import RegiaoResources, CidadeResources

from domain.localizacao.models import Regiao, Cidade


class CidadeAdmin(ImportExportModelAdmin):
    resource_class = CidadeResources
    list_display = ['nome', 'estado', 'regiao', 'slug']
    list_filter = ['regiao__nome']
    prepopulated_fields = {'slug': ('nome',)}


class RegiaoAdmin(ImportExportModelAdmin):
    resource_class = RegiaoResources
    list_display = ['nome', 'estado', 'slug']
    search_fields = ['nome']
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Regiao, RegiaoAdmin)

from django.contrib.gis.db import models


class Propriedade(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(decimal_places=2, max_digits=12)
    tipo = models.ForeignKey('imovel.Tipo', on_delete=models.PROTECT)
    foto = models.FileField()
    posicao = models.PointField('posicao', srid=4326, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

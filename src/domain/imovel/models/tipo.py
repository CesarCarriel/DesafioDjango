from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

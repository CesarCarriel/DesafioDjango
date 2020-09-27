from django.db import models
from django.db.models.signals import pre_save
from domain.localizacao.utils import unique_slug_generator


class Regiao(models.Model):
    slug = models.SlugField(max_length=250, null=True, blank=True)
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


def save_nome_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(save_nome_slug, sender=Regiao)

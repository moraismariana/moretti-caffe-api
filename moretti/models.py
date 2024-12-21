from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from moretti.mixins import DeleteOldImageMixin

# Classes para o Cardápio

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Prato(DeleteOldImageMixin, models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=10)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='moretti/pratos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='pratos')

    def __str__(self):
        return self.nome


# Classes para Estatísticas de visitantes

class Acesso(models.Model):
    revisita = models.BooleanField(default=False)

    acesso_cardapio = models.BooleanField(default=False)
    acesso_pagina_inicial = models.BooleanField(default=False)
    acesso_sobre = models.BooleanField(default=False)

    toque_contato = models.BooleanField(default=False)

    data = models.DateField(auto_now_add=True)

class EstatisticasGerais(models.Model):
    acessos = models.BigIntegerField(default=0, null=False, blank=False)
    revisitas = models.BigIntegerField(default=0, null=False, blank=False)

    acessos_cardapio = models.BigIntegerField(default=0, null=False, blank=False)
    acessos_pagina_inicial = models.BigIntegerField(default=0, null=False, blank=False)
    acessos_sobre = models.BigIntegerField(default=0, null=False, blank=False)

    toques_link_contato = models.BigIntegerField(default=0, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.pk and EstatisticasGerais.objects.exists():
            raise ValidationError("Já existe uma instância de configuração.")
        super().save(*args, **kwargs)

# Signal para atualizar Estatistica após salvar um Acesso
@receiver(post_save, sender=Acesso)
def atualizar_estatisticas_apos_criar(sender, instance, created, **kwargs):
    if created:
        estatistica, _ = EstatisticasGerais.objects.get_or_create(id=1)
        estatistica.acessos += 1
        estatistica.revisitas += 1 if instance.revisita else 0
        estatistica.acessos_cardapio += 1 if instance.acesso_cardapio else 0
        estatistica.acessos_pagina_inicial += 1 if instance.acesso_pagina_inicial else 0
        estatistica.acessos_sobre += 1 if instance.acesso_sobre else 0
        estatistica.toques_link_contato += 1 if instance.toque_contato else 0
        estatistica.save()


# Classes para edição de conteúdo CMS

class SingletonModel(models.Model):
    """Classe abstrata para garantir que apenas uma instância do modelo exista."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f"Já existe uma instância de {self.__class__.__name__}.")
        super().save(*args, **kwargs)


# Início
class InicioTexto(SingletonModel):
    introducao_titulo = models.TextField()
    introducao_subtitulo = models.TextField()
    banner1_titulo = models.TextField()
    banner2_titulo = models.TextField()
    banner3_titulo = models.TextField()
    localizacao_endereco = models.TextField()

class InicioBg(DeleteOldImageMixin, SingletonModel):
    introducao = models.ImageField(upload_to='moretti/cms')
    banner1 = models.ImageField(upload_to='moretti/cms')
    banner2 = models.ImageField(upload_to='moretti/cms')
    banner3 = models.ImageField(upload_to='moretti/cms')

# Sobre
class SobreTexto(SingletonModel):
    introducao_titulo = models.TextField()
    introducao_subtitulo = models.TextField()
    texto1 = models.TextField()
    texto2 = models.TextField()
    texto3 = models.TextField()
    texto4 = models.TextField()

class SobreBg(DeleteOldImageMixin, SingletonModel):
    introducao = models.ImageField(upload_to='moretti/cms')

class SobreImg(DeleteOldImageMixin, SingletonModel):
    fundador = models.ImageField(upload_to='moretti/cms')

# Cardápio
class CardapioTexto(SingletonModel):
    introducao_titulo = models.TextField()
    introducao_subtitulo = models.TextField()

class CardapioBg(DeleteOldImageMixin, SingletonModel):
    introducao = models.ImageField(upload_to='moretti/cms')
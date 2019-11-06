from django.db import models
from django.urls import reverse


class Inscricao(models.Model):
    nome = models.CharField('Nome', max_length=60)
    slug = models.SlugField('Identificador', max_length=60)
    descricao = models.TextField('Descricao', blank=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos:inscricao', kwargs={'slug': self.slug})
from django.contrib import admin
from .models import(
    Encontreiro,
    Encontrista,
    Equipe,
    Circulo,
    Contato
)
from produtos.models import Inscricao


class EncontreiroAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf', 'email', 'data_nascimento', 'celular')
    list_display = ('nome', 'cpf', 'email', 'data_nascimento', 'celular')
    list_filter = ['data_cadastro']


class EncontristaAdmin(admin.ModelAdmin):
    search_fields = ('nome_apelido', 'cpf','email', 'data_nascimento_enc', 'celular')
    list_display = ('nome_apelido', 'cpf', 'email', 'data_nascimento_enc', 'celular')
    list_filter = ['data_cadastro']


class InscricaoAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'descricao','preco')
    list_display = ('nome', 'descricao','preco')
    list_filter = ['created']


admin.site.register(Encontreiro, EncontreiroAdmin)
admin.site.register(Encontrista, EncontristaAdmin)
admin.site.register(Equipe)
admin.site.register(Circulo)
admin.site.register(Contato)
admin.site.register(Inscricao, InscricaoAdmin)
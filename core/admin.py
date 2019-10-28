from django.contrib import admin
from .models import(
    Encontreiro,
    Encontrista,
    Equipe,
    Circulo
)


class EncontreiroAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf', 'email', 'data_nascimento', 'celular')
    list_display = ('nome', 'cpf', 'email', 'data_nascimento', 'celular')


class EncontristaAdmin(admin.ModelAdmin):
    search_fields = ('nome_apelido', 'cpf','email', 'data_nascimento_enc', 'celular')
    list_display = ('nome_apelido', 'cpf', 'email', 'data_nascimento_enc', 'celular')


admin.site.register(Encontreiro, EncontreiroAdmin)
admin.site.register(Encontrista, EncontristaAdmin)
admin.site.register(Equipe)
admin.site.register(Circulo)
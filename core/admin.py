from django.contrib import admin
from .models import(
    Encontreiro,
    Encontrista,
    Equipe,
    Circulo
)


class EncontreiroAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email')
    list_display = ('nome', 'email')


class EncontristaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email', 'cpf')
    list_display = ('nome', 'email', 'cpf')


admin.site.register(Encontreiro, EncontreiroAdmin)
admin.site.register(Encontrista, EncontristaAdmin)
admin.site.register(Equipe)
admin.site.register(Circulo)
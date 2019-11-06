from django.shortcuts import render
from .models import Inscricao


def lista_inscricoes(request):
    context = {
        'lista_inscricoes': Inscricao.objects.all()
    }
    return render(request, 'produtos/lista_inscricoes.html', context)


def inscricao(request, slug):
    inscricao = Inscricao.objects.get(slug=slug)
    context = {
        'inscricao': inscricao,
    }
    return render(request, 'produtos/inscricao.html', context)
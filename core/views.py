from django.shortcuts import render, redirect
from .forms import EncontreiroForm, EncontristaForm, ContatoForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Contato
from django.contrib import messages


User = get_user_model()


def home(request):
    return render(request, 'index.html')

"""
def contato(request):
    success = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        #form.save()
        form.send_main()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success,
        }

    return render(request, 'contato.html', context)"""


def contato(request):
    if request.method == 'POST':
        contato = {}
        contato['nome'] = request.POST.get('nome')
        contato['telefone'] = request.POST.get('telefone')
        contato['email'] = request.POST.get('email')
        contato['mensagem'] = request.POST.get('mensagem')

        Contato.objects.create(**contato)
    return render(request, '_contato.html')


def encontreiro_novo(request):
    #import pdb;pdb.set_trace()
    form = EncontreiroForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_home')


def encontrista_novo(request):
    form = EncontristaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_home')


def login_admin(request):
    return redirect('admin/')




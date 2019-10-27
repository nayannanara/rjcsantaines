from django.shortcuts import render, redirect
from .forms import EncontreiroForm, EncontristaForm

from .models import *


def home(request):
    return render(request, 'index.html')


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


def login(request):
    return redirect('admin/')
from django import forms
from django.forms import ModelForm
from .models import Encontrista, Encontreiro


class EncontreiroForm(ModelForm):
    class Meta:
        model = Encontreiro
        fields = '__all__'


class EncontristaForm(ModelForm):
    class Meta:
        model = Encontrista
        fields = '__all__'
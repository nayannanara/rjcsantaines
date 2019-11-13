from django import forms
from django.forms import ModelForm
from .models import Encontrista, Encontreiro
from django.core.mail import send_mail
from django.conf import settings


class EncontreiroForm(ModelForm):
    class Meta:
        model = Encontreiro
        fields = '__all__'


class EncontristaForm(ModelForm):
    class Meta:
        model = Encontrista
        fields = '__all__'


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='Email')
    celular = forms.CharField(label='Celular')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)



    """ def send_main(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        celular = self.cleaned_data['celular']
        mensagem = self.cleaned_data['mensagem']
        msg = 'Nome: {0}\nE-mail: {1}\nCelular: {2}\nMensagem: {3}\n'.format(nome, email, celular, mensagem)
        send_mail(
            'Contato RJC - Santa Inês', msg, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]


    #def __init__(self, *args, **kwargs):
        #super(ContatoForm, self).__init__(*args, **kwargs)
        #self.fields['nome'].widget.attrs['class'] = 'form-control'
        #self.fields['email'].widget.attrs['class'] = 'form-control'
        #self.fields['celular'].widget.attrs['class'] = 'form-control'
        #self.fields['mensagem'].widget.attrs['class'] = 'form-control'"""

from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_inscricoes, name='lista_inscricoes'),
    path('<slug:slug>/', views.inscricao, name='inscricao'),
    #path('produtos/<slug:slug>/', views.product, name='product'),
]
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('alterar-senha/', views.update_password, name='accounts_update_password'),
    path('alterar-dados/', views.update_user, name='accounts_update_user'),
    path('registro/', views.accounts_register, name='accounts_registro'),
    path('', views.accounts_index, name='accounts_index'),

]
from django.urls import path
from .views import home, encontreiro_novo, encontrista_novo, login

urlpatterns =[
    path('', home, name='core_home'),
    path('encontreiro-novo', encontreiro_novo, name='core_encontreiro_novo'),
    path('encontrista-novo', encontrista_novo, name='core_encontrista_novo'),
    path('login', login, name='core_login' )
]
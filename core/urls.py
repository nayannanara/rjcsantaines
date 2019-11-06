from django.urls import path, include
from core import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path('',views.home, name='core_home'),
    path('encontreiro-novo', views.encontreiro_novo, name='core_encontreiro_novo'),
    path('encontrista-novo', views.encontrista_novo, name='core_encontrista_novo'),
    path('loginadmin', views.login_admin, name='core_login_admin'),
    path('contato', views.contato, name='core_contato'),
    path('login/', LoginView.as_view(template_name='login.html'), name='core_login'),
    path('logout/', LogoutView.as_view(next_page='core_home'), name='core_logout'),
    path('conta/',  include('accounts.urls', namespace='accounts')),
    path('compras/',  include('checkout.urls', namespace='checkout')),
    path('inscricoes/', include('produtos.urls', namespace='produtos')),
]
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from .models import User
from .forms import UserAdminCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'
    login_url = "/login/"


class CadastroView(CreateView):
    form_class = UserAdminCreationForm
    template_name = 'accounts/cadastro.html'
    model = User
    success_url = reverse_lazy('core_login')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('accounts:accounts_index')
    login_url = "/login/"

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:accounts_index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


accounts_index = IndexView.as_view()
accounts_register = CadastroView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
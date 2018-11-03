from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import PessoaFisicaSignUpForm
from ..models import User


class PessoaFisicaSignUpView(CreateView):
    model = User
    form_class = PessoaFisicaSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Pessoa Física'
        kwargs['form'] = PessoaFisicaSignUpForm()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home:index')

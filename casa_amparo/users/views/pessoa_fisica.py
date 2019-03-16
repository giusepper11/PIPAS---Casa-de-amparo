from allauth.account import app_settings
from allauth.account.utils import passthrough_next_redirect_url
from allauth.account.views import SignupView
from allauth.utils import get_request_param
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from ..forms import PessoaFisicaSignUpForm


class PessoaFisicaSignUpView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup.html'
    # the previously created form class
    form_class = PessoaFisicaSignUpForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'pessoa_fisica_signup'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_style'] = 'login-page'
        return context


# Create the view (we will reference to it in the url patterns)
pessoa_fisica_signup = PessoaFisicaSignUpView.as_view()

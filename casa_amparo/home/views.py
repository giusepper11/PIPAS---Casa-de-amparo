from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test


def user_is_not_logged_in(user):
    return not user.is_authenticated


# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_class'] = 'landing-page'
        return context


class AboutUsView(TemplateView):
    template_name = 'home/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_class'] = 'about-us'
        return context


@method_decorator([user_passes_test(user_is_not_logged_in, '/')], name='dispatch')
class SignupProfileView(TemplateView):
    template_name = 'home/profile_signup_select.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_style'] = 'signup-page'
        return context

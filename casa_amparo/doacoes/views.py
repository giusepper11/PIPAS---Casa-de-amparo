from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from casa_amparo.doacoes.forms import DoacaoOutrosForm, DemandaDoacaoForm
from casa_amparo.doacoes.models import DemandaDoacao, DoacaoUser
# Create your views here.
from casa_amparo.instituicoes.models import InstituicaoLista
from casa_amparo.users.decorators import instituicao_required
from casa_amparo.users.models import CustomUser
from casa_amparo.utils.utils import send_html_mail


class DoacaoOutrosCreateView(CreateView):
    template_name = 'doacoes/doacoes_outros_create.html'
    form_class = DoacaoOutrosForm
    success_url = 'donation_dashboard'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.instituicao = InstituicaoLista.objects.get(id=self.kwargs.get('inst_pk'))
        self.object.save()
        subject = "Oferta de doação de {}".format(self.object.nome)
        html_message = render_to_string('doacoes/emails/oferta_doacao_outros_email.html',
                                        context={'doador': self.object})
        send_html_mail(subject, html_message, [self.object.instituicao.user_inst.pf.user.email])
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.request.session['inst_id'] = kwargs.get('inst_pk')
        return super().get(self, request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inst_id'] = self.request.session.get('inst_id')
        return context


    def get_success_url(self):
        return reverse('instituicoes:inst_detail', kwargs={'pk': self.kwargs.get('inst_pk')})


@method_decorator([login_required, instituicao_required], name='dispatch')
class DoacaoDashboardView(CreateView):
    model = DemandaDoacao
    template_name = 'doacoes/donation_dashboard.html'
    form_class = DemandaDoacaoForm

    def get_success_url(self):
        return reverse('doacoes:doacao_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_style'] = 'profile-page'
        context['donations'] = DemandaDoacao.objects.filter(instituicao__user_inst__pf__user__id=self.request.user.id)
        context['donations_offer'] = DoacaoUser.objects.filter(
            demanda__instituicao__user_inst__pf__user__id=self.request.user.id)

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.instituicao = InstituicaoLista.objects.get(user_inst__pf__user__id=self.request.user.id)
        self.object.save()
        return super().form_valid(form)


class DoacoesUpdatelView(UpdateView):
    context_object_name = 'doacao'
    model = DemandaDoacao
    template_name = 'doacoes/modal_donation_update.html'
    form_class = DemandaDoacaoForm
    success_url = 'donation_dashboard'

    def get_queryset(self):
        donations = super().get_queryset()
        return donations.filter(instituicao__user_inst__pf__user__id=self.request.user.id)


class UserDonate(CreateView):
    template_name = 'doacoes/modal_offer_donation.html'
    model = DoacaoUser
    fields = ('obs',)

    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        self.request.session['inst_id'] = kwargs.get('inst_pk')
        self.request.session['donation_id'] = kwargs.get('donation_pk')
        return super().get(self, request, args, kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.demanda = DemandaDoacao.objects.get(id=self.request.session.get('donation_id'))
        self.object.doador = CustomUser.objects.get(id=self.request.user.id)
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('instituicoes:inst_detail', kwargs={'pk': self.request.session.get('inst_id')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inst_id'] = self.request.session.get('inst_id')
        context['donation_id'] = self.request.session.get('donation_id')
        return context

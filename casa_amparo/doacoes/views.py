from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from casa_amparo.doacoes.forms import DoacaoOutrosForm, DemandaDoacaoForm
from casa_amparo.doacoes.models import DemandaDoacao
# Create your views here.
from casa_amparo.instituicoes.models import InstituicaoLista
from casa_amparo.users.decorators import instituicao_required


class DoacaoOutrosCreateView(CreateView):
    template_name = 'doacoes/doacoes_outros_create.html'
    form_class = DoacaoOutrosForm
    success_url = 'donation_dashboard'


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
    #
    # def form_valid(self, form):
    #     super().form_valid(form)
    #     print("To aqui")
    #     return reverse('doacoes:doacao_dashboard')
    # #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    #

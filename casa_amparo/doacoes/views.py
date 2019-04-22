from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from casa_amparo.doacoes.forms import DoacaoOutrosForm
from casa_amparo.doacoes.models import DemandaDoacao

# Create your views here.
from casa_amparo.users.decorators import instituicao_required


class DoacoesDetailView(DetailView):
    context_object_name = 'doacao'
    model = DemandaDoacao
    template_name = 'doacoes/offer_donation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DoacaoOutrosCreateView(CreateView):
    template_name = 'doacoes/doacoes_outros_create.html'
    form_class = DoacaoOutrosForm


@method_decorator([login_required, instituicao_required], name='dispatch')
class DoacaoDashboardView(ListView):
    model = DemandaDoacao
    template_name = 'doacoes/donation_dashboard.html'

    def get_queryset(self):
        return self.model.objects.filter(instituicao__user_inst__pf__user__id=self.request.user.id)

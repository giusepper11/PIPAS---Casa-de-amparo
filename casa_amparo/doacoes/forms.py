from django import forms

from casa_amparo.doacoes.models import DoacaoOutros, DemandaDoacao


class DoacaoOutrosForm(forms.ModelForm):
    class Meta:
        model = DoacaoOutros
        exclude = ('doador', 'instituicao',)


class DemandaDoacaoForm(forms.ModelForm):
    class Meta:
        model = DemandaDoacao
        fields = ('doacao', 'qtd', 'obs', 'recebido')

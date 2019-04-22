from django import forms

from casa_amparo.doacoes.models import DoacaoOutros


class DoacaoOutrosForm(forms.ModelForm):

    class Meta:
        model = DoacaoOutros
        exclude = ('doador','instituicao',)

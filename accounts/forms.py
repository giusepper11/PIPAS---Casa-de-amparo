from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.db import transaction
from localflavor.br.forms import BRCPFField
from accounts.models import Cidade, Estado
from accounts.models import PessoaJuridica, PessoaFisica, User


class PessoaFisicaSignUpForm(UserCreationForm):

    nome = forms.CharField(
        label='Nome Completo',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Digite seu nome completo'}
        )
    )

    cpf = BRCPFField(
        label='CPF',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}
        )

    )

    endereco = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu endereço'}
        )
    )

    bairro = forms.CharField(
        label='Bairro',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu bairro'}
        )
    )

    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        widget=forms.Select(
            attrs={'class': 'selectpicker', 'data-style':"select-with-transition"}
        )
    )

    cidade = forms.ModelChoiceField(
        queryset=Cidade.objects.all(),
        widget=forms.Select(
            attrs={'class': 'selectpicker', 'data-style':"select-with-transition"}
        )
    )

    cep = forms.CharField(
        label='CEP',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu CEP'}
        )
    )

    profile_pic = forms.ImageField(
        label='Foto',
        required=False,
        widget=forms.FileInput(

        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label_dict = {
            'username': 'Digite um nome de usuário',
            'email': 'Digite seu e-mail',
            'password1': 'Digite uma senha',
            'password2':'Confirme sua senha'
        }
        for field_name, field in self.fields.items():
            if field_name in self.Meta.fields:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = label_dict.get(field_name, '')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_pf = True
        user.save()
        PessoaFisica.objects.create(user=user, cpf=self.cleaned_data['cpf'])

        return user

from allauth.account.forms import SignupForm
from allauth.utils import set_form_field_order
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.db import transaction
from localflavor.br.forms import BRCPFField, BRZipCodeField
from users.models import Cidade, Estado
from users.models import PessoaJuridica, PessoaFisica, CustomUser


class PessoaFisicaSignUpForm(SignupForm):
    nome = forms.CharField(
        label='Nome Completo',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}
        )
    )

    cpf = BRCPFField(
        label='CPF',
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}
        )

    )

    endereco = forms.CharField(
        label='Endereço',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu endereço'}
        )
    )

    bairro = forms.CharField(
        label='Bairro',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu bairro'}
        )
    )

    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'selectpicker', 'data-style': "select-with-transition"}
        )
    )

    cidade = forms.ModelChoiceField(
        queryset=Cidade.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'selectpicker', 'data-style': "select-with-transition"}
        )
    )

    cep = BRZipCodeField(
        label='CEP',
        required=True,
        max_length=9,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu CEP'}
        )
    )

    profile_pic = forms.ImageField(
        label='Foto',
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'fileinput'}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        field_order = ['email', 'password1', 'password2', ]
        set_form_field_order(self, field_order)

    # Override the save method to save the extra fields
    # (otherwise the form will save the User instance only)
    @transaction.atomic
    def save(self, request):
        # Save the User instance and get a reference to it
        self.cleaned_data['is_pf'] = True
        user = super().save(request)
        # Create an instance of your model with the extra fields
        # then save it.
        # (N.B: the are already cleaned, but if you want to do some
        # extra cleaning just override the clean method as usual)
        pessoa_fisica = PessoaFisica(
            user=user,
            cpf=self.cleaned_data.get('cpf'),
            nome=self.cleaned_data.get('nome'),
            endereco=self.cleaned_data.get('endereco'),
            bairro=self.cleaned_data.get('bairro'),
            estado=self.cleaned_data.get('estado'),
            cidade=self.cleaned_data.get('cidade'),
            cep=self.cleaned_data.get('cep'),
            profile_pic=self.cleaned_data.get('profile_pic'),
        )
        pessoa_fisica.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return pessoa_fisica.user

import email
from pyexpat import model
from django import forms
from django.forms import fields, models
from .models import Perfil, Endereco
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(sefl):
        e = sefl.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está em uso.'.format(e))
        
        return e

class PerfilForm(forms.ModelForm):
    data_De_Nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        ) 
    )
    class Meta:
        model = Perfil
        fields = ['nome_Completo', 'cpf', 'data_De_Nascimento', 'num_Do_Cartao_Do_Sus', 'telefone', 'usuario']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['endereco', 'num_Da_Residencia', 'complemento', 'bairro', 'cep', 'ponto_De_Referencia', 'usuario']

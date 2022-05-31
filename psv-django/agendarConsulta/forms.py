from django import forms
from django.forms import fields, models
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        ) 
    )
    class Meta:
        model = Pessoa
        fields = ('numero_cartao_sus','cpf','nome_completo','data','telefone')

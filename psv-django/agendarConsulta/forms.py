from django import forms
from django.forms import fields, models
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    data_De_Nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        ) 
    )
    class Meta:
        model = Pessoa
        fields = ('numero_Do_Cartao_Do_SUS','cPF','data_De_Nascimento','endereco','numero_Da_Residencia', 'complemento', 'bairro', 'telefone', 'cEP', 'ponto_De_Referencia')

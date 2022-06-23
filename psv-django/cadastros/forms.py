from django import forms
from django.forms import fields, models
from .models import Pessoa, Endereco, AgendarConsulta, Medico, Consulta, Agendamento

class PessoaForm(forms.ModelForm):
    data_De_Nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        ) 
    )
    class Meta:
        model = Pessoa
        fields = ('nome_Completo', 'cpf', 'data_De_Nascimento', 'num_Do_Cartao_Do_Sus')

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('endereco', 'num_Da_Residencia', 'complemento', 'bairro', 'telefone', 'cep', 'ponto_De_Referencia', 'pessoa')

class AgendarConsultaForm(forms.ModelForm):
    class Meta:
        model = AgendarConsulta
        fields = ('tipo_Da_Consulta', 'turno', 'dia_Da_Semana', 'status')

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nome_Completo', 'crm', 'especializacao', 'turno', 'dia_Da_Semana', 'email', 'senha')
        widgets = {
        'senha': forms.PasswordInput(),
    }

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('descricao', 'tipo_Da_Consulta', 'medico')

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ('turno', 'consulta', 'medico')
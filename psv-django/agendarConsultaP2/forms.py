from django import forms
from django.forms import fields, models
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ('tipo_Da_Consulta','turno','dia_Da_Semana','status')
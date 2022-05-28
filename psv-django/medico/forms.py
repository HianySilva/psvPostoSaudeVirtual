from django import forms
from django.forms import fields, models
from .models import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nome_completo','crm','especializacao','turno','email','senha')
        widgets = {
        'senha': forms.PasswordInput(),
    }

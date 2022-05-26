from django import forms
from .models import Medico

class formMedico(forms.ModelForm):
    class Meta:
        model = Medico
        field= ('nome','crm','especializacao','turno','email','senha')

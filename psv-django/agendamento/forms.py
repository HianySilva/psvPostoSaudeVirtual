from django import forms
from django.forms import fields, models
from .models import Agendar, SemanaList, TurnoList

class AgendarForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Agendar
        fields = ('tipo_consulta','data')

class AgendarSemana(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = SemanaList
        fields = ('Semana',)


class AgendarTurno(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = TurnoList
        fields = ('List',)


        
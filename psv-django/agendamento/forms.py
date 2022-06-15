from django import forms
from django.forms import fields, models
from .models import Agendar, SemanaList, TurnoList

class DateInput(forms.DateInput):
    input_type = 'date'

class AgendarForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Agendar
        fields = ('tipo_consulta','data', 'year_in_school')
        widgets = {
            'data': DateInput()
        }
        

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


        
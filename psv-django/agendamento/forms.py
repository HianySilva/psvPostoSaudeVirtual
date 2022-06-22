#from django import forms
#from django.forms import fields, models
#from .models import Agendar, TurnoList

#class DateInput(forms.DateInput):
#    input_type = 'date'

#class AgendarForm(forms.ModelForm):
#    required_css_class = 'required'
#    class Meta:
#        model = Agendar
#        fields = ('tipo_consulta','data', 'dia_da_semana','turno')
#        widgets = {
#            'data': DateInput()
#        }
        



#class AgendarTurno(forms.ModelForm):
#    required_css_class = 'required'
#    class Meta:
#        model = TurnoList
#        fields = ('List',)        
from django import forms
from django.forms import fields, models
from .models import  SemanaList

class AgendarSemana(forms.ModelForm):
    class Meta:
        model = SemanaList
        fields = ('Semana',)

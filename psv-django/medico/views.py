from django.shortcuts import render
from django.views.generic import ListView
from .models import Medico

class ListaMedicoView(ListView):
    model = Medico
    queryset = Medico.objects.all().order_by('nome_completo')


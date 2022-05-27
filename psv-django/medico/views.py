import imp
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Medico
from .forms import MedicoForm

class ListaMedicoView(ListView):
    model = Medico
    queryset = Medico.objects.all().order_by('nome_completo')

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    success_url = '/medicos/'
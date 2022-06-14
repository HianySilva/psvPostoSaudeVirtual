from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Agendar,SemanaList
from .forms import AgendarForm, AgendarSemana

# Create your views here.
class AgendarCreateView(CreateView):
    model = Agendar
    form_class = AgendarForm
    success_url = '/agendamento/'

class SemanaCreateView(CreateView):
    model = SemanaList
    form_class = AgendarSemana
    success_url = '/agendamento/'
    
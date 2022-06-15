from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Agendar
from .forms import AgendarForm

# Create your views here.
class AgendarCreateView(CreateView):
    model = Agendar
    form_class = AgendarForm
    success_url = '/agendamento/'


    
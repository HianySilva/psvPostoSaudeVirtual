from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import SemanaList
from .forms import AgendarSemana

# Create your views here.

class SemanaCreateView(CreateView):
    model = SemanaList
    form_class = AgendarSemana
    success_url = '/semana/'
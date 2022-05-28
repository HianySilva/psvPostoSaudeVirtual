import imp
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Medico
from .forms import MedicoForm

class ListaMedicoView(ListView):
    model = Medico
    queryset = Medico.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset();
        filtro_nome =self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome) 
        return queryset

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    success_url = '/medicos/'

class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    success_url = '/medicos/'

class MedicoDeleteView(DeleteView):
    model = Medico
    success_url = '/medicos/'
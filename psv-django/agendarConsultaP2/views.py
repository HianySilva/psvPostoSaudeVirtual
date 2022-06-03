from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Agendamento
from .forms import AgendamentoForm

class ListaAgendamentoView(ListView):
    model = Agendamento
    queryset = Agendamento.objects.all().order_by('tipo_Da_Consulta')

    def get_queryset(self):
        queryset = super().get_queryset();
        filtro_tipo_Da_Consulta =self.request.GET.get('tipo_Da_Consulta') or None

        if filtro_tipo_Da_Consulta:
            queryset = queryset.filter(cPF__contains=filtro_tipo_Da_Consulta) 
        return queryset 

class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    success_url = '/agendarConsultaP2/'

class AgendamentoUpdateView(UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    success_url = '/agendarConsultaP2/'

class AgendamentoDeleteView(DeleteView):
    model: Agendamento
    success_url = '/agendarConsultaP2/'

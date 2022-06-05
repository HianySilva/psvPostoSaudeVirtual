from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class FuncionalidadesView(TemplateView):
    template_name = 'funcionalidades.html'

class Consultar_agendarView(TemplateView):
    template_name = 'Consultar_agendar.html'


from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Medico
class HomePageView(TemplateView):
    template_name = 'home.html'
    class ListaMedicoView(ListView):
        model = Medico
        queryset = Medico.objects.all().order_by('nome_completo')


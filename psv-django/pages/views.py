from django.views.generic import TemplateView
from django.views.generic import ListView
class HomePageView(TemplateView):
    template_name = 'home.html'
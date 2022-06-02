from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('funcionalidades/', login_required(views.FuncionalidadesView.as_view()), name='funcionalidades'),
    path('cadastrar_agendar/', login_required(views.Consultar_agendarView.as_view()), name='cadastrar_agendar'),
]
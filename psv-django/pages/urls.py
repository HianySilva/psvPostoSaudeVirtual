from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('funcionalidades/', views.FuncionalidadesView.as_view(), name='funcionalidades'),
    path('cadastrar_agendar/', views.Consultar_agendarView.as_view(), name='cadastrar_agendar'),
]
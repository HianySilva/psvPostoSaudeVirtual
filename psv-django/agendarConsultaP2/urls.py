from django.urls import path
from .views import ListaAgendamentoView, AgendamentoCreateView, AgendamentoUpdateView, AgendamentoDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns =  [
    path('', login_required(ListaAgendamentoView.as_view()), name='consulta.index'),
    path('novo/', login_required(AgendamentoCreateView.as_view()), name='consulta.novo'),
    path('editar/<int:pk>', login_required(AgendamentoUpdateView.as_view()), name='consulta.editar'),
    path('remover/<int:pk>', login_required(AgendamentoDeleteView.as_view()), name='consulta.remover'),
]
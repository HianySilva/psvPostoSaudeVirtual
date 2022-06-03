from django.urls import path
from .views import ListaAgendamentoView, AgendamentoCreateView, AgendamentoUpdateView, AgendamentoDeleteView

urlpatterns =  [
    path('', ListaAgendamentoView.as_view(), name='consulta.index'),
    path('novo/', AgendamentoCreateView.as_view(), name='consulta.novo'),
    path('editar/<int:pk>', AgendamentoUpdateView.as_view(), name='consulta.editar'),
    path('remover/<int:pk>', AgendamentoDeleteView.as_view(), name='consulta.remover'),
]
import imp
from django.urls import path
from .views import ListaMedicoView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView

urlpatterns = [
    path('', ListaMedicoView.as_view(), name='medico.index'),
    path('novo/', MedicoCreateView.as_view(), name='medico.novo'),
    path('editar/<int:pk>', MedicoUpdateView.as_view(), name='medico.editar'),
    path('remover/<int:pk>', MedicoDeleteView.as_view(), name='medico.remover'),
]
import imp
from django.urls import path
from .views import ListaMedicoView, MedicoCreateView

urlpatterns = [
    path('', ListaMedicoView.as_view(), name='medico.index'),
    path('novo/', MedicoCreateView.as_view(), name='medico.novo'),
]
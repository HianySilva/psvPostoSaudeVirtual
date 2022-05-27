import imp
from django.urls import path
from .views import ListaMedicoView

urlpatterns = [
    path('', ListaMedicoView.as_view(), name='medico.index')
]
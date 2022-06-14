from django.urls import path
from .views import AgendarCreateView, SemanaCreateView

urlpatterns =  [
    path('', AgendarCreateView.as_view(), name='agenda.index'),
    path('', SemanaCreateView.as_view(), name='semana'),
 
]
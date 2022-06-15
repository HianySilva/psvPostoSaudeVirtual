from django.urls import path
from .views import AgendarCreateView

urlpatterns =  [
    path('', AgendarCreateView.as_view(), name='agenda.index'),

 
]
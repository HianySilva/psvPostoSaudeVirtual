#import imp
#from django.urls import path
#from .views import ListaMedicoView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView
#from django.contrib.auth.decorators import login_required

#urlpatterns = [
#    path('', ListaMedicoView.as_view(), name='medico.index'),
#    path('novo/', login_required(MedicoCreateView.as_view()), name='medico.novo'),
#    path('editar/<int:pk>', login_required(MedicoUpdateView.as_view()), name='medico.editar'),
#    path('remover/<int:pk>', login_required(MedicoDeleteView.as_view()), name='medico.remover'),
#]
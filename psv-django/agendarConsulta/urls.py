from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns =  [
    path('', login_required(ListaPessoaView.as_view()), name='pessoa.index'),
    path('novo/', login_required(PessoaCreateView.as_view()), name='pessoa.novo'),
    path('editar/<int:pk>', login_required(PessoaUpdateView.as_view()), name='pessoa.editar'),
    path('remover/<int:pk>', login_required(PessoaDeleteView.as_view()), name='pessoa.remover'),
]
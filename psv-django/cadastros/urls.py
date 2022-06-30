from django.urls import path
from .views import PessoaCreateView, EnderecoCreateView, AgendarConsultaCreateView, MedicoCreateView, ConsultaCreateView, AgendamentoCreateView, PessoaUpdateView, EnderecoUpdateView, AgendarConsultaUpdateView, MedicoUpdateView, ConsultaUpdateView, AgendamentoUpdateView, PessoaDeleteView, EnderecoDeleteView, AgendarConsultaDeleteView, MedicoDeleteView, ConsultaDeleteView, AgendamentoDeleteView, AgendarConsultarListView ,AgendamentoListView, MedicoListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('cadastrar/pessoa/', login_required(PessoaCreateView.as_view()), name='cadastar-pessoa'),
    path('cadastrar/endereco/', login_required(EnderecoCreateView.as_view()), name='cadastar-endereco'),
    path('cadastrar/tipoConsulta/', login_required(AgendarConsultaCreateView.as_view()), name='cadastar-tipo-consulta'),
    path('cadastrar/medico/', login_required(MedicoCreateView.as_view()), name='cadastar-medico'),
    path('cadastrar/descricao/', login_required(ConsultaCreateView.as_view()), name='cadastar-consulta-descricao'),
    path('cadastrar/agendamento/', login_required(AgendamentoCreateView.as_view()), name='cadastar-agendamento'),

    path('editar/pessoa/<int:pk>', login_required(PessoaUpdateView.as_view()), name='editar-pessoa'),
    path('editar/endereco/<int:pk>', login_required(EnderecoUpdateView.as_view()), name='editar-endereco'),
    path('editar/tipoConsulta/<int:pk>', login_required(AgendarConsultaUpdateView.as_view()), name='editar-tipo-consulta'),
    path('editar/medico/<int:pk>', login_required(MedicoUpdateView.as_view()), name='editar-medico'),
    path('editar/descricao/<int:pk>', login_required(ConsultaUpdateView.as_view()), name='editar-consulta-descricao'),
    path('editar/agendamento/<int:pk>', login_required(AgendamentoUpdateView.as_view()), name='editar-agendamento'),

    path('deletar/pessoa/<int:pk>', login_required(PessoaDeleteView.as_view()), name='deletar-pessoa'),
    path('deletar/endereco/<int:pk>', login_required(EnderecoDeleteView.as_view()), name='deletar-endereco'),
    path('deletar/tipoConsulta/<int:pk>', login_required(AgendarConsultaDeleteView.as_view()), name='deletar-tipo-consulta'),
    path('deletar/medico/<int:pk>', login_required(MedicoDeleteView.as_view()), name='deletar-medico'),
    path('deletar/descricao/<int:pk>', login_required(ConsultaDeleteView.as_view()), name='deletar-consulta-descricao'),
    path('deletar/agendamento/<int:pk>', login_required(AgendamentoDeleteView.as_view()), name='deletar-agendamento'),

    path('listar/tipoConsulta/', login_required(AgendarConsultarListView.as_view()), name='listar-tipo-consulta'),
    path('listar/agendamento/', login_required(AgendamentoListView.as_view()), name='listar-agendamento'),
    path('listar/medico/', MedicoListView.as_view(), name='listar-medico'),
]
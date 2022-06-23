import imp
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Pessoa, Endereco, AgendarConsulta, Medico, Consulta, Agendamento
from .forms import PessoaForm, EnderecoForm, AgendarConsultaForm, MedicoForm, ConsultaForm, AgendamentoForm
from braces.views import GroupRequiredMixin

############### CREATEVIEW ##################################

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/cadastros/cadastrar/endereco/'
    template_name = 'cadastros/cadastro.html'

class EnderecoCreateView(CreateView):
    model = Endereco
    form_class = EnderecoForm
    def get_success_url(self):
        return reverse_lazy ('cadastar-agendamento')
    template_name = 'cadastros/cadastro.html'

class AgendarConsultaCreateView(GroupRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = AgendarConsulta
    form_class = AgendarConsultaForm
    success_url = '/cadastros/cadastrar/medico/'
    template_name = 'cadastros/cadastro.html'

class MedicoCreateView(GroupRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Medico
    form_class = MedicoForm
    success_url = '/cadastros/cadastrar/descricao/'
    template_name = 'cadastros/cadastro.html'

class ConsultaCreateView(GroupRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Consulta
    form_class = ConsultaForm
    success_url = '/cadastros/cadastrar/agendamento/'
    template_name = 'cadastros/cadastro.html'

class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    success_url = '/cadastros/listar/agendamento/'
    template_name = 'cadastros/agendamento.html'

############### UPDATEVIEW ##################################

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/'
    template_name = 'cadastros/agendamento.html'

class EnderecoUpdateView(UpdateView):
    model = Endereco
    form_class = EnderecoForm
    success_url = '/'
    template_name = 'cadastros/agendamento.html'

class AgendarConsultaUpdateView(GroupRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = AgendarConsulta
    form_class = AgendarConsultaForm
    success_url = '/'
    template_name = 'cadastros/agendamento.html'

class MedicoUpdateView(GroupRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Medico
    form_class = MedicoForm
    success_url = '/'
    template_name = 'cadastros/agendamento.html'

class ConsultaUpdateView(GroupRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Consulta
    form_class = ConsultaForm
    success_url = '/'
    template_name = 'cadastros/agendamento.html'

class AgendamentoUpdateView(UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    success_url = '/'
    template_name = 'cadastros/agendamento.html'

############### DELETEVIEW ##################################

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/'
    template_name = 'cadastros/forms-excluir.html'

class EnderecoDeleteView(DeleteView):
    model = Endereco
    success_url = '/'
    template_name = 'cadastros/forms-excluir.html'

class AgendarConsultaDeleteView(GroupRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = AgendarConsulta
    success_url = '/'
    template_name = 'cadastros/forms-excluir.html'

class MedicoDeleteView(GroupRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Medico
    success_url = '/'
    template_name = 'cadastros/forms-excluir.html'

class ConsultaDeleteView(GroupRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Consulta
    success_url = '/'
    template_name = 'cadastros/forms-excluir.html'

class AgendamentoDeleteView(DeleteView):
    model = Agendamento
    success_url = '/'
    template_name = 'cadastros/forms-excluir.html'

############### LISTVIEW ##################################

class AgendarConsultarListView(ListView):
    model = AgendarConsulta
    template_name = 'cadastros/listas/tipoConsulta.html'

class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'cadastros/listas/agendamentoList.html'
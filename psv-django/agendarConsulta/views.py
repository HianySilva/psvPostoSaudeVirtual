#from django.shortcuts import render
#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from .models import Pessoa
#from .forms import PessoaForm

#class ListaPessoaView(ListView):
#    model = Pessoa
#    queryset =Pessoa.objects.all().order_by('nome_Completo')

#    def get_queryset(self):
#        queryset = super().get_queryset();
#        filtro_nome =self.request.GET.get('nome') or None

#        if filtro_nome:
#            queryset = queryset.filter(cPF__contains=filtro_nome) 
#        return queryset

#class PessoaCreateView(CreateView):
#    model = Pessoa
#    form_class = PessoaForm
#    success_url = '/agendarConsulta/'

#class PessoaUpdateView(UpdateView):
#    model = Pessoa
#    form_class = PessoaForm
#    success_url = '/agendarConsulta/'

#class PessoaDeleteView(DeleteView):
#    model = Pessoa
#    success_url = '/agendarConsulta/'
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from requests import request
from .forms import EnderecoForm, UsuarioForm, PerfilForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil, Endereco

class UsuarioCreate(CreateView):
    template_name = 'account/signup.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Visitante')
        
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)
        Endereco.objects.create(usuario=self.object)

        return url

class PerfilUpdateView(UpdateView):
    template_name = 'cadastros/cadastro.html'
    model = Perfil
    form_class = PerfilForm
    success_url = reverse_lazy('atualizar-endereco')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)

        return self.object

class EnderecoUpdateView(UpdateView):
    template_name = 'cadastros/cadastro.html'
    model = Endereco
    form_class = EnderecoForm
    success_url = reverse_lazy('cadastar-agendamento')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Endereco, usuario=self.request.user)

        return self.object
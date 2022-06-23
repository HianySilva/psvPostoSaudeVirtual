from django.contrib import admin
from .models import Perfil, Endereco

class PerfilAdmin(admin.ModelAdmin):
    list_display = [
        'nome_Completo',
        'cpf',
        'data_De_Nascimento',
        'num_Do_Cartao_Do_Sus',
        'telefone',
        'usuario'
    ]

class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        'endereco',
        'num_Da_Residencia',
        'complemento',
        'bairro',
        'cep',
        'ponto_De_Referencia',
        'usuario'
    ]

    search_fields = [
        'nome_completo'
    ]


admin.site.register(Perfil)
admin.site.register(Endereco)
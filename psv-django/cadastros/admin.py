from django.contrib import admin
from .models import Pessoa, Endereco, AgendarConsulta, Medico, Consulta, Agendamento

class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_Completo',
        'cpf',
        'data_De_Nascimento',
        'num_Do_Cartao_Do_Sus'
    ]
    
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        'endereco',
        'num_Da_Residencia',
        'complemento',
        'bairro',
        'telefone',
        'cep',
        'ponto_De_Referencia',
        'pessoa'
    ]

class AgendarConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'tipo_Da_Consulta',
        'turno',
        'dia_Da_Semana',
        'status'
    ]

class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_Completo',
        'crm'
        'especializacao',
        'turno',
        'dia_Da_Semana',
        'email',
        'senha'
    ]    

class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'descricao',
        'agendarConsulta',
        'medico'
    ]

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = [
        'pessoa',
        'endereco',
        'agendarConsulta',
        'consulta',
        'medico'
    ]    

    search_fields = [
        'nome_completo'
    ]
    
admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(AgendarConsulta)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Agendamento)
from django.contrib import admin
from .models import Agendamento

# Register your models here.

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = [
        'tipo_Da_Consulta',
        'turno',
        'dia_Da_Semana',
        'status',
    ]

    list_filter = [
        'status'
    ]

    search_fields = [
        'tipo_Da_Consulta'
    ]


admin.site.register(Agendamento, AgendamentoAdmin)
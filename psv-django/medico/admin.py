from django.contrib import admin
from .models import Medico

# Register your models here.

class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'crm',
        'especializacao',
        'turno',
        'email',
        'senha'
    ]

    search_fields = [
        'nome_completo'
    ]


admin.site.register(Medico, MedicoAdmin)

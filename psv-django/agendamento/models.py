from django.db import models
from enum import Enum

class TipoConsulta(models.Model):
    descricao = models.CharField(max_length=256)

class TurnoList(models.Model):
    MANHA = 'MN'
    TARDE = 'TD'
    NOITE = 'NT'
    TList =[
    (MANHA, 'Manhã'),
    (TARDE, 'Tarde'),
    (NOITE, 'Noite'),
    ]
    List = models.CharField(max_length=256, choices = TList)
    
class Agendar(models.Model):
    SEGUNDA = 'SD'
    TERCA = 'TC'
    QUARTA = 'QR'
    QUINTA = 'QI'
    SEXTA = 'ST'

    MANHA = 'MH'
    TARDE = 'TD'
    NOITE = 'NT'
    
    tipo_consulta = models.ForeignKey (TipoConsulta, on_delete=models.CASCADE)
    data = models.DateField()
    DIA_DA_SEMANA_CHOICES = (
        (SEGUNDA, 'Segunda'),
        (TERCA, 'Terça'),
        (QUARTA, 'Quarta'),
        (QUINTA, 'Quinta'),
        (SEXTA, 'Sexta'),
    )
    dia_da_semana = models.CharField(
        max_length=2,
        choices=DIA_DA_SEMANA_CHOICES,
        default=SEGUNDA,
        blank=True,
        null=True
    , )

    TURNO_CHOICES = (
        (MANHA, 'Manhã'),
        (TARDE, 'Tarde'),
        (NOITE, 'Noite'),
    )
    turno = models.CharField(
        max_length=2,
        choices=TURNO_CHOICES,
        default=MANHA,
        blank=True,
        null=True
    , )

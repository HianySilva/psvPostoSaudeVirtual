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
    

class SemanaList(models.Model):
    SEGUNDA = 'SEG'
    TERCA = 'TERC'
    QUARTA = 'QUAR'
    QUINTA =' QUIN'
    SEXTA = 'SEX'
    SList =[
        (SEGUNDA, 'Segunda'),
        (TERCA, 'Terça'),
        (QUARTA, 'Quarta'),
        (QUINTA, 'Quinta'),
        (SEXTA,  'Sexta'), 
    ]
    Semana = models.CharField(max_length=256, choices = SList)

class Agendar(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    
    tipo_consulta = models.ForeignKey (TipoConsulta, on_delete=models.CASCADE)
    data = models.DateField()
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
        blank=True,
        null=True
    , )

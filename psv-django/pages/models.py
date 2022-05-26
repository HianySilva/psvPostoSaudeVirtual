from django.db import models

# Create your models here.
class Medico (models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=200)
    especializacao = models.CharField(max_length=200)
    turno = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
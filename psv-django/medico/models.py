from django.db import models
class Medico (models.Model):
    nome_completo = models.CharField(max_length=256)
    crm = models.CharField(max_length=256)
    especializacao = models.CharField(max_length=256)
    turno = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    senha = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome_completo
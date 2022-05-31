from django.db import models

class Pessoa(models.Model):
    numero_cartao_sus = models.CharField(max_length=256)
    cpf = models.CharField(max_length=256)
    nome_completo = models.CharField(max_length=256)
    data = models.DateField(null=True)
    telefone = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome_completo
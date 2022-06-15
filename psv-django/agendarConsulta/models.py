from django.db import models

class Pessoa(models.Model):
    numero_Do_Cartao_Do_SUS = models.CharField(max_length=256)
    cPF = models.CharField(max_length=256)
    data_De_Nascimento = models.DateField(null=True)
    endereco = models.CharField(max_length=256)
    numero_Da_Residencia = models.CharField(max_length=256)
    complemento = models.CharField(max_length=256)
    bairro = models.CharField(max_length=256)
    telefone = models.CharField(max_length=256)
    cEP = models.CharField(max_length=256)
    ponto_De_Referencia = models.TextField(max_length=256)

    def __str__(self) -> str:
        return self.cPF
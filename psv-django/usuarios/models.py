from django.db import models
from django.contrib.auth.models import User 

class Perfil(models.Model):
    nome_Completo = models.CharField(max_length=256, null=True)
    cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True, null=True)
    data_De_Nascimento = models.DateField(null=True)
    num_Do_Cartao_Do_Sus = models.CharField(verbose_name='Número Do Cartão do SUS' ,max_length=19, unique=True, null=True)
    telefone = models.CharField(max_length=15, unique=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

class Endereco(models.Model):
    endereco = models.CharField(verbose_name='Endereço' ,max_length=2560, null=True)
    num_Da_Residencia = models.CharField(verbose_name='Número da Residência', max_length=2, null=True)
    complemento = models.CharField(max_length=256, null=True)
    bairro = models.CharField(max_length=256, null=True)
    cep = models.CharField(verbose_name='CEP', max_length=9, null=True)
    ponto_De_Referencia = models.TextField(verbose_name='Ponto de Referência', max_length=256, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
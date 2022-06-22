#from django.db import models

#class Pessoa(models.Model):
#    nome_Completo = models.CharField(max_length=256, null=True, blank=True)
#    numero_Do_Cartao_Do_SUS = models.CharField(max_length=256, verbose_name='Número Do Cartão Do SUS')
#    cPF = models.CharField(max_length=256)
#    data_De_Nascimento = models.DateField(null=True, verbose_name='Data De Nascimento')
#    endereco = models.CharField(max_length=256, verbose_name='Endereço')
#    numero_Da_Residencia = models.CharField(max_length=256, verbose_name='Número Da Residência')
#    complemento = models.CharField(max_length=256)
#    bairro = models.CharField(max_length=256)
#    telefone = models.CharField(max_length=256)
#    cEP = models.CharField(max_length=256)
#    ponto_De_Referencia = models.TextField(max_length=256, verbose_name='Ponto De Referência')

#    def __str__(self) -> str:
#        return self.nome_Completo
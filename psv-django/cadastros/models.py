from django.db import models


class Pessoa(models.Model):
    nome_Completo = models.CharField(max_length=256)
    cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True)
    data_De_Nascimento = models.DateField()
    num_Do_Cartao_Do_Sus = models.CharField(verbose_name='Número Do Cartão do SUS' ,max_length=19, unique=True)

    def __str__(self):
        return self.nome_Completo

class Endereco(models.Model):
    endereco = models.CharField(verbose_name='Endereço' ,max_length=2560)
    num_Da_Residencia = models.CharField(verbose_name='Número da Residência', max_length=2)
    complemento = models.CharField(max_length=256)
    bairro = models.CharField(max_length=256)
    telefone = models.CharField(max_length=15, unique=True)
    cep = models.CharField(verbose_name='CEP', max_length=9)
    ponto_De_Referencia = models.TextField(verbose_name='Ponto de Referência', max_length=256)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.endereco, self.num_Da_Residencia)

class AgendarConsulta(models.Model):
    tipo_Da_Consulta = models.CharField(max_length=256, unique=True)
    turno = models.CharField(max_length=5)
    dia_Da_Semana = models.CharField(max_length=13)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{} ({})".format(self.turno, self.tipo_Da_Consulta)

class Medico(models.Model):
    nome_Completo = models.CharField(max_length=256)
    crm = models.CharField(verbose_name='CRM', max_length=256, unique=True)
    especializacao = models.CharField(verbose_name='Especialização', max_length=256)
    turno = models.CharField(max_length=5)
    dia_Da_Semana = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    senha = models.CharField(max_length=256)

    def __str__(self):
        return self.nome_Completo

class Consulta(models.Model):
    descricao = models.TextField(verbose_name='Descrição' ,max_length=256, null=True, blank=True)
    tipo_Da_Consulta = models.ForeignKey(AgendarConsulta, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{}: {}".format(self.tipo_Da_Consulta.tipo_Da_Consulta, self.descricao)

class Agendamento(models.Model):
    SEGUNDA = 'SD'
    TERCA = 'TC'
    QUARTA = 'QR'
    QUINTA = 'QI'
    SEXTA = 'ST'


    nome_De_Usuario = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
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

    turno = models.ForeignKey(AgendarConsulta, on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome_Completo

# Generated by Django 3.2.13 on 2022-06-21 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendarConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_Da_Consulta', models.CharField(max_length=256)),
                ('turno', models.CharField(max_length=5)),
                ('dia_Da_Semana', models.CharField(max_length=7)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_Completo', models.CharField(max_length=256)),
                ('crm', models.CharField(max_length=256, verbose_name='CRM')),
                ('especializacao', models.CharField(max_length=256, verbose_name='Especialização')),
                ('turno', models.CharField(max_length=5)),
                ('dia_Da_Semana', models.CharField(max_length=7)),
                ('email', models.EmailField(max_length=256)),
                ('senha', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_Completo', models.CharField(max_length=256)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('data_De_Nascimento', models.DateField()),
                ('num_Do_Cartao_Do_Sus', models.CharField(max_length=19, verbose_name='Número Do Cartão do SUS')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=2560, verbose_name='Endereço')),
                ('num_Da_Residencia', models.CharField(max_length=2, verbose_name='Número da Residência')),
                ('complemento', models.CharField(max_length=256)),
                ('bairro', models.CharField(max_length=256)),
                ('telefone', models.CharField(max_length=15)),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('ponto_De_Referencia', models.TextField(max_length=256, verbose_name='Ponto de Referência')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=256, verbose_name='Descrição')),
                ('agendarConsulta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.agendarconsulta')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agendarConsulta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.agendarconsulta')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.consulta')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.endereco')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.medico')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.pessoa')),
            ],
        ),
    ]
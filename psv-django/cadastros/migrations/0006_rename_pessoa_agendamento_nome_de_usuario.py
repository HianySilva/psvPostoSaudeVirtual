# Generated by Django 3.2.13 on 2022-06-22 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_rename_consulta_consulta_tipo_da_consulta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='pessoa',
            new_name='nome_De_Usuario',
        ),
    ]

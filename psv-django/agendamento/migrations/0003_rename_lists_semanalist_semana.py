# Generated by Django 3.2.13 on 2022-06-13 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0002_remove_agendar_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semanalist',
            old_name='ListS',
            new_name='Semana',
        ),
    ]

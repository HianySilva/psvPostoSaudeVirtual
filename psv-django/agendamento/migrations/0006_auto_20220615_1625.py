# Generated by Django 3.2.13 on 2022-06-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0005_alter_agendar_year_in_school'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SemanaList',
        ),
        migrations.AlterField(
            model_name='agendar',
            name='year_in_school',
            field=models.CharField(blank=True, choices=[('SD', 'Segunda'), ('TC', 'Terca'), ('QR', 'Quanta'), ('QI', 'Quinta'), ('ST', 'Sexta')], default='SD', max_length=2, null=True),
        ),
    ]

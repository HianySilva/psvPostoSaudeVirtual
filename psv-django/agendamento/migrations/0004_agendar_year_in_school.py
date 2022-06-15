# Generated by Django 3.2.13 on 2022-06-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0003_rename_lists_semanalist_semana'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendar',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
# Generated by Django 3.2.13 on 2022-06-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SemanaList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semana', models.CharField(choices=[('SEG', 'Segunda'), ('TERC', 'Terça'), ('QUAR', 'Quarta'), (' QUIN', 'Quinta'), ('SEX', 'Sexta')], max_length=256)),
            ],
        ),
    ]
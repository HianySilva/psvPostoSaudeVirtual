# Generated by Django 3.2.13 on 2022-06-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendarConsulta', '0002_auto_20220615_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='nome_Completo',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
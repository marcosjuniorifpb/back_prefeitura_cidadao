# Generated by Django 5.1 on 2024-08-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenciamento", "0006_autorização_uso_de_solo_eventual"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autorização_uso_de_solo_eventual",
            name="Requerente",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="sedrub",
            name="Endereco",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="sedrub",
            name="Requerente",
            field=models.CharField(max_length=200),
        ),
    ]

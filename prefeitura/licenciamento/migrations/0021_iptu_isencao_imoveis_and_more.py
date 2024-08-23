# Generated by Django 5.1 on 2024-08-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenciamento", "0020_rename_sedrub_sedrub_autorizacao_uso_solo_comercial"),
    ]

    operations = [
        migrations.CreateModel(
            name="IPTU_Isencao_Imoveis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Descricao", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Atualizacao_Cadatral_Dos_Quiosques",
        ),
        migrations.DeleteModel(
            name="Autorizacao_Uso_de_Solo_Eventual",
        ),
        migrations.DeleteModel(
            name="SEDRUB_Autorizacao_Uso_Solo_Comercial",
        ),
    ]
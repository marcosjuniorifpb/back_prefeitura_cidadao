# Generated by Django 5.1 on 2024-08-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "licenciamento_2",
            "0017_alter_atualizacao_cadatral_dos_quiosques_tempo_ocupa_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="atualizacao_cadatral_dos_quiosques",
            name="Tipo_Construcao",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
# Generated by Django 5.0 on 2024-08-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0011_familia_acolhedora_forms_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="bairro",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="celular",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="cep",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="cidade",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="complemento",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="cpf",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="data_nascimento",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="email",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="endereco",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="genero_acolhimento",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="idade",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="mensagem",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="nome",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="numero_residencia",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="ponto_referencia",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="preferencia_perfil",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="renda",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="renda_aproximada",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="residente",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="rg",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="sabendo_servico",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="telefone",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora_forms",
            name="uf",
            field=models.CharField(max_length=10),
        ),
    ]
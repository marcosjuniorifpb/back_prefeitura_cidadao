# Generated by Django 5.0 on 2024-08-21 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0006_alter_familia_acolhedora_data_nascimneto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="data_nascimneto",
            field=models.DateField(default=0),
        ),
    ]
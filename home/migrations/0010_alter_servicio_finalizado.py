# Generated by Django 4.2.13 on 2024-06-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_servicio_finalizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='finalizado',
            field=models.DateField(blank=True, null=True),
        ),
    ]

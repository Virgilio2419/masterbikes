# Generated by Django 4.2.13 on 2024-06-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cliente_newsletter_alter_cliente_registrado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='newsletter',
            field=models.BooleanField(),
        ),
    ]

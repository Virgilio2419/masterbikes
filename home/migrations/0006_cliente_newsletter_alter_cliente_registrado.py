# Generated by Django 4.2.13 on 2024-06-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='newsletter',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='registrado',
            field=models.BooleanField(),
        ),
    ]

# Generated by Django 4.2.13 on 2024-07-03 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_venta_tipo_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

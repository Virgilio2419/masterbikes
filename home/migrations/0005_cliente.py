# Generated by Django 4.2.13 on 2024-06-25 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_bicicleta_color_servicio_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(choices=[('1', 'Cerrillos'), ('2', 'Cerro Navia'), ('3', 'Conchalí'), ('4', 'El Bosque'), ('5', 'Estación Central'), ('6', 'Huechuraba'), ('7', 'Independencia'), ('8', 'La Cisterna'), ('9', 'La Florida'), ('10', 'La Granja'), ('11', 'La Pintana'), ('12', 'La Reina'), ('13', 'Las Condes'), ('14', 'Lo Barnechea'), ('15', 'Lo Espejo'), ('16', 'Lo Prado'), ('17', 'Macul'), ('18', 'Maipú'), ('19', 'Ñuñoa'), ('20', 'Pedro Aguirre Cerda'), ('21', 'Peñalolén'), ('22', 'Providencia'), ('23', 'Pudahuel'), ('24', 'Quilicura'), ('25', 'Quinta Normal'), ('26', 'Recoleta'), ('27', 'Renca'), ('28', 'San Joaquín'), ('29', 'San Miguel'), ('30', 'San Ramón'), ('31', 'Santiago'), ('32', 'Vitacura')], max_length=2)),
                ('registrado', models.IntegerField()),
                ('usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]

from django.db import models

# Create your models here.

class Vehiculo(models.Model):
	marca = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)
	anio = models.IntegerField()
	precio = models.IntegerField()
	hp = models.IntegerField()
	color = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.marca} {self.modelo}"

class Instrumento(models.Model):
	Tipo = models.CharField(max_length=100)
	marca = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)
	precio = models.IntegerField()
	color = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.Tipo} {self.modelo}"


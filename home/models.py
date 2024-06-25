from django.db import models

# Create your models here.

class  Bicicleta(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    aro = models.IntegerField()
    marca = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="img",null=True)
    
    def __str__(self):
        return self.marca
    
class Servicio(models.Model):
    cod = models.IntegerField()
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    aro = models.IntegerField()
    marca = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="img",null=True)
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    mail = models.EmailField()
    valor_cotizado = models.IntegerField()
    valor_repuestos = models.IntegerField()
    valor_final= models.IntegerField()
    METODO_PAGO_CHOICES = [
        ("1", "Efectivo"),
        ("2", "Debito"),
        ("3", "Credito"),
    ]
    metodo_pago = models.CharField(max_length=1, choices=METODO_PAGO_CHOICES)
    ingreso = models.DateField()
    estado= models.IntegerField()
    comentarios = models.CharField(max_length=300)
    finalizado = models.DateField()

    
    def __str__(self):
        return f"{self.cod} {self.marca} {self.nombre_completo} "
    
    
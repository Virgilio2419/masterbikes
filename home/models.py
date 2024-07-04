from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class  Bicicleta(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    aro = models.IntegerField()
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100,null=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="img",null=True)
    
    def __str__(self):
        return self.marca
    
class Producto(models.Model):
    tipo_choices = [
        ("1", "Bicicleta"),
        ("2", "Casco"),
        ("3", "Guantes")
    ]
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    aro = models.IntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    imagen = models.ImageField(upload_to="img", null=True, blank=True)
    
    def __str__(self):
        return self.tipo
    

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
    estados_CHOICES = [
        ("1", "Ingresado"),
        ("2", "En Proceso"),
        ("3", "Finalizado"),
        ("4", "Entregado"),
    ]
    estado = models.CharField(max_length=1, choices=estados_CHOICES)
    comentarios = models.CharField(max_length=300)
    finalizado = models.DateField(null=True)

    
    def __str__(self):
        return f"{self.cod} {self.marca} {self.nombre_completo} "
    

class Cliente(models.Model):
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    mail = models.EmailField()
    direccion = models.CharField(max_length=100)
    COMUNA_CHOICES = [
    ("1", "Cerrillos"),
    ("2", "Cerro Navia"),
    ("3", "Conchalí"),
    ("4", "El Bosque"),
    ("5", "Estación Central"),
    ("6", "Huechuraba"),
    ("7", "Independencia"),
    ("8", "La Cisterna"),
    ("9", "La Florida"),
    ("10", "La Granja"),
    ("11", "La Pintana"),
    ("12", "La Reina"),
    ("13", "Las Condes"),
    ("14", "Lo Barnechea"),
    ("15", "Lo Espejo"),
    ("16", "Lo Prado"),
    ("17", "Macul"),
    ("18", "Maipú"),
    ("19", "Ñuñoa"),
    ("20", "Pedro Aguirre Cerda"),
    ("21", "Peñalolén"),
    ("22", "Providencia"),
    ("23", "Pudahuel"),
    ("24", "Quilicura"),
    ("25", "Quinta Normal"),
    ("26", "Recoleta"),
    ("27", "Renca"),
    ("28", "San Joaquín"),
    ("29", "San Miguel"),
    ("30", "San Ramón"),
    ("31", "Santiago"),
    ("32", "Vitacura"),
]
    comuna = models.CharField(max_length=2, choices=COMUNA_CHOICES)
    registrado = models.BooleanField()
    newsletter = models.BooleanField()
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"RUT: {self.rut}-{self.dv} Nombre: {self.nombre_completo}"
  
class Servicio(models.Model):
    cod = models.ForeignKey(Cliente, on_delete=models.CASCADE)
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
    estados_CHOICES = [
        ("1", "Ingresado"),
        ("2", "En Proceso"),
        ("3", "Finalizado"),
        ("4", "Entregado"),
    ]
    estado = models.CharField(max_length=1, choices=estados_CHOICES)
    comentarios = models.CharField(max_length=300)
    finalizado = models.DateField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.cod} {self.marca} {self.nombre_completo} "
    def save(self, *args, **kwargs):
        self.valor_final = self.valor_cotizado + self.valor_repuestos
        super().save(*args, **kwargs)

    ##VENTAS
    
class Venta(models.Model):
    tipo_choices = [
    ("1", "Bicicleta"),
    ("2", "Casco"),
    ("3", "Guantes")]
    tipo_producto = models.CharField(max_length=2, choices=tipo_choices)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(default=timezone.now)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.precio_venta * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.Producto} vendida a {self.cliente.nombre} por {self.vendedor}'
        

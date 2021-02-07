from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Representante(models.Model):
    ci = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telf = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ["apellido"]
    
    def __str__(self) :
        return str(self.apellido)

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telf = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    nucleo = models.CharField(max_length=50)
    representante_id = models.ForeignKey(Representante, on_delete=models.CASCADE, db_constraint=False)
    
    class Meta:
        ordering = ["apellido"]
    
    def __str__(self) :
        return str(self.apellido)

class Instrumento(models.Model):
    FAMILIA = [
        ('CUE', 'Cuerdas'),
        ('VMA', 'Viento-Madera'),
        ('VME', 'Viento_Metal'),
        ('PER', 'Percusion'),
    ]
    serial = models.CharField(max_length=1000, primary_key=True)
    sin_fundamusical = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    familia = models.CharField(max_length=13, choices=FAMILIA)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["nombre"]
    
    def __str__(self) :
        return str(self.serial)

class Comodato(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now)
    instrumento_serial = models.ForeignKey(Instrumento, on_delete=models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["fecha"]
    
    def __str__(self) :
        return str(self.instrumento_serial)


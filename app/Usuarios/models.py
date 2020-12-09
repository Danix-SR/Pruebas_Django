from django.db import models

# Create your models here.

class Usuario (models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.EmailField()
    Contraseña = models.CharField(max_length=50)
    Rol = models.CharField(max_length=50)
    Estado = models.BooleanField()


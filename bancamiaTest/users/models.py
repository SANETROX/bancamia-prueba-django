from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES = (
    ("cc","cc"),
    ("ti","ti")
)

# Create your models here.
class UserBancamia(AbstractUser):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    numero_documento = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=10,choices=CHOICES)
    fecha_nacimiento = models.DateTimeField()
    ciudad_nacimiento = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=10)


    def __str__(self):
        return f'{self.username}'

from django.db import models

class MyModel(models.Model):
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
    Motivo = models.CharField(max_length=100)
    Mensaje = models.TextField()

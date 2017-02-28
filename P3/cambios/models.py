from __future__ import unicode_literals

from django.db import models

# Create your models  DE la palicacion cambios.

class Datos(models.Model):
    nombre = models.CharField(max_length=50);
    descripcion = models.TextField()
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    image = models.ImageField(upload_to="media/imagenes")
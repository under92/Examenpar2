from django.db import models
from datetime import datetime

# Create your models here.
class investigacion(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    categoria = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'investigacion'


class categoria_investigacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __srt__ (self):   
        return self.nombre
# Create your models here.
from django.db import models
from django.conf import settings


class PostIt(models.Model):

    titulo = models.CharField(
        max_length=100
    )

    detalle = models.TextField()

    completada = models.BooleanField(
        default=False
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null=True, blank=True
    )


    def __str__(self):
        return self.titulo
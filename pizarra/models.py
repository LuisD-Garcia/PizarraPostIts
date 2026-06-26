
# Create your models here.
from django.db import models


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


    def __str__(self):
        return self.titulo
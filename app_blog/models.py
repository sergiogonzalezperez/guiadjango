from django.db import models

# Create your models here.
from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)  # Título de la publicación
    contenido = models.TextField()             # Contenido
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)  # Fecha automática

    def __str__(self):
        return self.titulo  # Muestra el título en el admin
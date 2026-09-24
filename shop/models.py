from django.db import models
from django.contrib.auth.models import User

class pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10, choices=[
        ('G', 'General'),
        ('PG', 'Apto para todo público'),
        ('PG-13', 'Apto para mayores de 13 años'),
        ('R', 'Restringido'),
        ('NC-17', 'No apto para menores de 17 años')
    ])
    

    def __str__(self):
        return self.titulo
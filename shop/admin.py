from django.contrib import admin

from .models import pelicula

@admin.register(pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'fecha_lanzamiento')
    list_filter = ('genero', 'clasificacion')
    search_fields = ('titulo', 'descripcion')

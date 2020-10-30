from django.db import models

class tareas(models.Model):
    titulo = models.CharField('Título', max_length=200)
    descripcion = models.CharField('Descripción', max_length=600)
    fecha_creacion = models.DateTimeField('Fecha creación', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField('Fecha actualización', auto_now=True)

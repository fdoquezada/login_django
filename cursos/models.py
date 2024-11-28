from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField(help_text="duracion en horas")
    
    
    def __str__(self):
        return self.nombre
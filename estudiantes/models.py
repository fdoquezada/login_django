from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    edad = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.email}"

# Create your models here.

from django.db import models

# Create your models here.



class Abono(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Fanatico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    abono_origen_id = models.ForeignKey(Abono, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
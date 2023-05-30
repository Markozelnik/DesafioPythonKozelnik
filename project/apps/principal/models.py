from django.db import models

# Create your models here.


class PrincipalCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    asignacion= models.CharField(max_length=250, null=True,)


    def __str__(self):
        return self.nombre
from django.db import models

class  ProductoCategoriaList (models.Model):
    nombre = models.CharField (max_lenght=50)#aca estaria la extra
    
    def __str__(self):
        return self.nombre
    
class MerchCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "categoría de merch"
        verbose_name_plural = "categorías de merch"

    def __str__(self):
        return self.nombre

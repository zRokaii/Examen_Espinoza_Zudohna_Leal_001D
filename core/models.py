from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoría')

    def __str__(self):
        return self.nombreCategoria


class Casa(models.Model):
    direccion= models.CharField(max_length=50, primary_key=True, verbose_name='Dirección')
    comuna= models.CharField(max_length=50, verbose_name='Comuna')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion
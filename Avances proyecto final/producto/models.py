from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    CATEGORIAS = [
        ('COMIDA', 'Comida'),
        ('BEBIDA', 'Bebida'),
        ('ASEO', 'Aseo'),
        ('OTROS', 'Otros'),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OTROS')
    ubicacion = models.CharField(max_length=100, default='Desconocida')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.nombre

    def total_likes(self):
        return self.likes.count()

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.producto.nombre}'
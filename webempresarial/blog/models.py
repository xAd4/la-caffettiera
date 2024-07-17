from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

# OPTIMIZACIÓN DE CARPETA MEDIA
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = Blog.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'blog/' + filename

# Creación de categorías
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la categoría")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.name

# Creación de instancias de blog, con relaciones al "User" y al modelo "Category"
class Blog(models.Model):
    date = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    title = models.CharField(max_length=100, verbose_name="Título")
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, verbose_name="Imágen")
    content = models.TextField(verbose_name="Contenido")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuarios")
    categories = models.ManyToManyField(Category, related_name="get_posts", verbose_name="Categorías")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return self.title

# BORRA UNA FOTO AL BORRAR UNA INSTANCIA
@receiver(post_delete, sender=Blog)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)


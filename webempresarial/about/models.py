from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

# OPTIMIZACIÓN DE CARPETA MEDIA
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = About.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'about/' + filename

class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    subTitle = models.CharField(max_length=100, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Historia"
        verbose_name_plural = "Historias"
    
    def __str__(self):
        return self.title
    
# BORRA UNA FOTO AL BORRAR UNA INSTANCIA
@receiver(post_delete, sender=About)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

from django.db import models

# Create your models here.

class SectionOne(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    subTitle = models.CharField(max_length=100, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Sección / 1"
        verbose_name_plural = "Secciones / 1"
    
    def __str__(self):
        return self.title
    
###################################################################################################################

class SectionTwo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    subTitle = models.CharField(max_length=100, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Sección / 2"
        verbose_name_plural = "Secciones / 2"
    
    def __str__(self):
        return self.title


from django.db import models

# Create your models here.

class Social(models.Model):
    name = models.CharField(max_length=100, verbose_name="Red Social")
    url = models.URLField(max_length=500, verbose_name="URL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Social, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
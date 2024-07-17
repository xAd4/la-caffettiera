from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    email = models.EmailField(max_length=100, verbose_name="Email")
    phone_number = PhoneNumberField(verbose_name="Número de teléfono")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
    
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Store(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    week_days = models.CharField(max_length=100, verbose_name="Días de semana")
    week_days_schedule = models.CharField(max_length=100, verbose_name="Horario de días de semana")
    weekend = models.CharField(max_length=100, verbose_name="Fines de semana")
    weekend_schedule = models.CharField(max_length=100, verbose_name="Horario fines de semana")
    sunday = models.CharField(max_length=100, verbose_name="Domingos")
    sunday_schedule = models.CharField(max_length=100, verbose_name="Horario de los Domingos")
    address = models.CharField(max_length=100, verbose_name="Dirección del local")
    city = models.CharField(max_length=100, verbose_name="Ciudad de ubicación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return self.title



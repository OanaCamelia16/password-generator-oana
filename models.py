from django.db import models

class Generator(models.Model):
    Numar_total_de_caractere = models.IntegerField(default = 0)
    Numar_de_cifre = models.IntegerField(default = 0)
    Numar_caractere_speciale = models.IntegerField(default = 0)

# Create your models here.

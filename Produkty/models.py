from django.db import models

# Create your models here.
class Produkty(models.Model):
    nazwa = models.CharField(max_length=100)
    rocznik = models.DecimalField(max_digits=12, decimal_places=2)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    #SDSADSADASDAS

    def __str__(self):
        return self.nazwa

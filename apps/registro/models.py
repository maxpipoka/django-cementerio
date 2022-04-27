from django.db import models

# Create your models here.

class Contribuyente(models.Model):
    nombre = models.CharField(max_length=250, blank= False, null=False)
    dni= models.IntegerField(max_length=8, blank= False, null=False)
    direccion = models.CharField(max_length=250, blank= False, null=False)
from django.db import models

# Create your models here.

class Contribuyente(models.Model):
    nombre = models.CharField(max_length=250, blank= False, null=False)
    dni = models.IntegerField(max_length=8, blank= False, null=False)
    direccion = models.CharField(max_length=250, blank= False, null=False)
    
    class Meta:
        verbose_name = 'Contribuyente'
        verbose_name_plural = 'Contribuyentes'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    

class Usuario(models.Model):
    usuario = models.ForeignKey(Contribuyente, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=15, blank= False, null=False)
    nivel_acceso = models.IntegerField(max_length=1, null=False)
    is_active = models.BooleanField
    is_staff = models.BooleanField
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre_usuario']
        
    def __str__(self):
        return self.nombre_usuario
        

class Fallecido(models.Model):
    fallecido = models.ForeignKey(Contribuyente, on_delete=models.CASCADE)
    fecha_fallecimiento = models.DateField(blank=False, null=False)
    
    class Meta:
        verbose_name = 'Fallecido'
        verbose_name_plural= 'Fallecidos'
        ordering = ['fallecido']
        
    def __str__(self):
        return self.fallecido
    
    
    
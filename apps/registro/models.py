from django.db import models

# Create your models here.

class Contribuyente(models.Model):
    nombre = models.CharField(max_length=250, blank= False, null=False)
    dni = models.IntegerField(blank= False, null=False)
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
    nivel_acceso = models.IntegerField(blank=False, null=False)
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
    

class OficinaRegistro(models.Model):
    oficina_registro = models.CharField(max_length=100, blank=False, null=False)
    departamento_registro = models.CharField(max_length=100, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Of.Registro'
        verbose_name_plural= 'Ofs.Registro'
        ordering = ['departamento_registro']
        
    def __str__(self):
        return self.departamento_registro + '-' + self.oficina_registro

class PermisoInhumacion(models.Model):
    fecha_en_registro = models.DateField(blank=False, null=False)
    fecha_presentacion = models.DateField(blank=False, null=False)
    fallecido = models.ForeignKey(Fallecido, on_delete=models.PROTECT)
    presentado_por = models.ForeignKey(Contribuyente, on_delete=models.PROTECT)
    oficina_registro = models.ForeignKey(OficinaRegistro, on_delete=models.PROTECT)
    observaciones = models.TextField(blank=True, null=True)
    imagen = models.ImageField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Perm.Inhum'
        verbose_name_plural= 'Perms.Inhum'
        ordering = ['fecha_presentacion']
        
    def __str__(self):
        return self.fallecido + '-' + self.fecha_presentacion
    
class Zona(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        ordering = ['nombre']
        

class Periodicidad(models.Model):
    nombre = models.CharField(max_length=100, blank= False, null=False)
    cant_anios = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Periodicidad'
        verbose_name_plural = 'Periodicidades'
        ordering = ['nombre']
        
        
class Parcela(models.Model):
    numero = models.IntegerField(blank=False, null=False)
    fila = models.IntegerField(blank=False, null=False)
    sector = models.CharField(max_length=20, blank= False, null=False)
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT)
    
    def __str__(self):
        return (self.Zona + ' - ' + self.sector + '-' + self.fila + ' - N:' + self.numero)
    
    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
        

class Tasa(models.Model):
    nombre = models.CharField(max_length=100, blank= False, null=False)
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT)
    periodicidad = models.ForeignKey(Periodicidad, on_delete=models.PROTECT)
    monto = models.FloatField(blank=False, null=False)
    fecha_desde = models.DateTimeField(blank=False, null=False)
    fecha_hasta = models.DateTimeField(blank=False, null=False)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name = 'Tasa'
        verbose_name_plural = 'Tasas'
        

class Recibo(models.Model):
    numero_recibo = models.IntegerField(blank=False, null=False)
    monto_tasa = models.FloatField(blank=False,null=False)
    monto_recargo = models.FloatField(blank=True,null=True)    
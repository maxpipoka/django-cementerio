from django.contrib import admin
from .models import Contribuyente, Usuario, Fallecido, OficinaRegistro, PermisoInhumacion, Zona, Periodicidad, Parcela, Tasa, Recibo

# Register your models here.

admin.site.register(Contribuyente)
admin.site.register(Usuario)
admin.site.register(Fallecido)
admin.site.register(OficinaRegistro)
admin.site.register(PermisoInhumacion)
admin.site.register(Zona)
admin.site.register(Periodicidad)
admin.site.register(Parcela)
admin.site.register(Tasa)
admin.site.register(Recibo)

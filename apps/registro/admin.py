from django.contrib import admin
from .models import Contribuyente, Usuario, Fallecido

# Register your models here.

admin.site.register(Contribuyente)
admin.site.register(Usuario)
admin.site.register(Fallecido)

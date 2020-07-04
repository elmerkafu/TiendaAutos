from django.contrib import admin
from .models import Tipo, Marca, Modelo, Auto

# Register your models here.

admin.site.register(Tipo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Auto)


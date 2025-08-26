from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publicacion  # Importa el modelo

admin.site.register(Publicacion)  # Registra el modelo
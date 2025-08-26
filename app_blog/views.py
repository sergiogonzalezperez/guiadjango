from django.shortcuts import render
from .models import Publicacion  # Importa el modelo

def index(request):
    # Obtener todas las publicaciones de la base de datos
    publicaciones = Publicacion.objects.all()
    # Renderiza la plantilla y pasa los datos
    return render(request, 'app_blog/index.html', {'publicaciones': publicaciones})
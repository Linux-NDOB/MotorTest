from django.urls import path
from .views import  Propietarios, Motocicletas, Oficinas, Pruebas
app_name = "wen_app"

urlpatterns = [
    path('propietario/', Propietarios.as_view(), name = "propietario_lista"),
    path('propietario/<int:propietario_id>', Propietarios.as_view(), name = "propietario"),
    
    path('motocicleta/', Motocicletas.as_view(), name = "motos_lista"),
    path('motocicleta/<int:motocicleta_id>', Motocicletas.as_view(), name = "motocicleta"),
    
    path('oficina/', Oficinas.as_view(), name = "oficina_lista"),
    path('oficina/<int:oficina_id>', Oficinas.as_view(), name = "oficina"),
    
    path('prueba/', Pruebas.as_view(), name = "prueba_lista"),
    path('prueba/<int:prueba_id>', Pruebas.as_view(), name = "prueba"),
]
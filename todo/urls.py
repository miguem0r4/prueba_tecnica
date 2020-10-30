from django.urls import path
from todo.views import tareasListado, tareaDetalle, tareaCrear, tareaActualizar, tareaEliminar

from . import views

app_name = 'todo'
urlpatterns = [

    path('', tareasListado.as_view(template_name = "tareas/index.html"), name='leer'),
 
    path('detalle/<int:pk>', tareaDetalle.as_view(template_name = "tareas/detalles.html"), name='detalles'),
 
    path('crear', tareaCrear.as_view(template_name = "tareas/crear.html"), name='crear'),
 
    path('editar/<int:pk>', tareaActualizar.as_view(template_name = "tareas/actualizar.html"), name='actualizar'), 
 
    path('eliminar/<int:pk>', tareaEliminar.as_view(), name='eliminar'),     
]

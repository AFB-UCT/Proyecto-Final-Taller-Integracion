from django.urls import path
from . import views

urlpatterns = [
    path('obtener/', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregarProducto, name='producto_agregar'),
    path('', views.inicio, name='inicio'),
    path('obtener/<int:id>',views.porId,name='producto_mostrar'),
    path('eliminar/<int:id>',views.eliminarId, name='producto_eliminar'),
    path('actualizar/<int:id>',views.actualizarId, name='producto_actualizar'),
]

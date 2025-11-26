from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from producto import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed_view, name='feed'),
    path('crear/', views.crear_oferta_view, name='crear_oferta'),
    path('oferta/<int:id>/', views.detalle_oferta_view, name='detalle_oferta'),
    path('validar/<int:id>/', views.validar_oferta_view, name='validar_oferta'),
    
    # Rutas antiguas
    path('inicio/', views.inicio, name='inicio'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('obtener/<int:id>/', views.buscarID, name='buscarID'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('accounts/', include('django.contrib.auth.urls')), # Login/Logout
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


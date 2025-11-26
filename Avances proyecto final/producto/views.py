from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Comentario
from .forms import ProductoForm, ComentarioForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect('feed')

def feed_view(request):
    query = request.GET.get('q')
    categoria = request.GET.get('categoria')
    productos = Producto.objects.all().order_by('-fecha_publicacion')

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ubicacion__icontains=query)
        )
    
    if categoria:
        productos = productos.filter(categoria=categoria)

    return render(request, 'feed.html', {'productos': productos})

@login_required
def crear_oferta_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('feed')
    else:
        form = ProductoForm()
    return render(request, 'crear_oferta.html', {'form': form})

def detalle_oferta_view(request, id):
    producto = get_object_or_404(Producto, id=id)
    comentarios = producto.comentarios.all().order_by('-fecha')
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.producto = producto
            comentario.usuario = request.user
            comentario.save()
            return redirect('detalle_oferta', id=id)
    else:
        form = ComentarioForm()

    return render(request, 'detalle_oferta.html', {'producto': producto, 'comentarios': comentarios, 'form': form})

@login_required
def validar_oferta_view(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.user in producto.likes.all():
        producto.likes.remove(request.user)
    else:
        producto.likes.add(request.user)
    return redirect('detalle_oferta', id=id)

# Vistas antiguas mantenidas por compatibilidad o eliminadas si no se usan
def inicio(request):
    return render(request, 'inicio.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "listar.html", {'productos': productos})

def buscarID(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'mostrar.html', {'producto': producto})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    # Lógica de edición simplificada para este ejemplo
    return render(request, 'editar.html', {'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')
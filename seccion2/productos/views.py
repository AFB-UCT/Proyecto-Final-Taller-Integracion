from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto

# Create your views here.


def lista_productos(request):
    productos = Producto.objects.all()
    context = {"nombre":"Producto A",
                "descripcion":"Descripcion del producto A",
                  "cantidad":10,

                  'productos':productos}
    
    return render(request, 'productos/obtener_productos.html',
                  context)

def inicio(request):
    return render(request, 'productos/inicio.html')

def porId(request, id):
    #print(id)
    #producto = Producto.objects.get(id=id)
    producto = get_object_or_404(Producto, id=id)
    context={'producto':producto}
    return render(request, 'productos/productos_mostrar.html', context)

def eliminarId(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')

def actualizarId(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.cantidad = request.POST.get('cantidad')
        producto.save()
        return redirect('producto_mostrar', id=producto.id)
    else:
        context = {'producto': producto}
        return render(request, 'productos/producto_actualizar.html', context)

def agregarProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        cantidad = request.POST.get('cantidad')
        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, cantidad=cantidad)
        nuevo_producto.save()
        return redirect('lista_productos')
    else:
        return render(request, 'productos/agregar_producto.html')
from django.shortcuts import render,redirect
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse
# Create your views here.
def agregar_productos(request):
    #Checar si vengo desde el formulario enviado
    if request.method =='POST':
        #Mandaron el formulario
        form =productoForm(request.POST)
        #Validar que el formulario este correcto 
        if form.is_valid():
            #Si es valido entonces lo guardo
            form.save()
            return redirect('ver') #Redirecciona a la lista de productos
    #Si no vengo de enviar el formulario (si solo quiero ver)
    else :
        form=productoForm()
    #Vamos a pintar el formulario
    return render(request,'agregar_productos.html',{'form':form})    

def ver_producto(request):
    #Obtener de la base de datos todoso los productos
    productos=Producto.objects.all()
    #Estamos de volviendo u front un obejto desde el back
    return  render (request,'ver.html',{'productos':productos})

#Esta funcion pinta el html que carga los productos con json
def index(request):
    return render(request,'productos.html')

#esta funcion que devuelve todod los productos como un JSON
def lista_productos(request):
    productos=Producto.objects.all()
     #Generar un diccionario al aire que ordena los productos

    data=[
         {
            'nombre':p.nombre,
            'precio':p.precio,
            'imagen':p.imagen,
         }
         for p in productos
     ]
    return JsonResponse(data,safe=False)
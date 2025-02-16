from django.shortcuts import render,redirect
from .models import Categoria
from .forms import categoriasForm
from django.http import JsonResponse
# Create your views here.
def agregar_categoria(request):
    #Checar si vengo desde el formulario enviado
    if request.method =='POST':
        #Mandaron el formulario
        form =categoriasForm(request.POST)
        #Validar que el formulario este correcto 
        if form.is_valid():
            #Si es valido entonces lo guardo
            form.save()
            return redirect('ver') #Redirecciona a la lista de categoria
    #Si no vengo de enviar el formulario (si solo quiero ver)
    else :
        form=categoriasForm()
    #Vamos a pintar el formulario
    return render(request,'agregar_categoria.html',{'form':form})    

def ver_categoria(request):
    #Obtener de la base de datos todoso los productos
    categoria=Categoria.objects.all()
    #Estamos de volviendo u front un obejto desde el back
    return  render (request,'ver_categoria.html',{'categorias':categoria})

#Esta funcion pinta el html que carga los productos con json
def index(request):
    return render(request,'categoria.html')

#esta funcion que devuelve todod los productos como un JSON
def lista_categoria(request):
    categoria=Categoria.objects.all()
     #Generar un diccionario al aire que ordena los productos

    data=[
         {
            'nombre':c.nombre,
            'imagen':c.imagen,
         }
         for c in categoria
     ]
    return JsonResponse(data,safe=False)
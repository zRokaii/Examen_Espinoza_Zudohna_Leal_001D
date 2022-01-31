from django.shortcuts import render, redirect
from django.views.decorators import csrf
from rest_framework.serializers import Serializer
from .models import Casa
from .forms import CasaForm

# Create your views here.

def home(request):
    nombre= 'Claudia Andrea'

    casas = Casa.objects.all()

    return render(request, 'home.html', context={'nom_usuario': nombre, 'datos': casas}
    )

def crearVehiculo(request):
    if request.method=='POST': 
        casa_form = CasaForm(request.POST)
        if casa_form.is_valid():
            casa_form.save()
            return redirect('home')
    else:
        casa_form= CasaForm()
    return render(request, 'core/form_crearvehiculo.html', {'casa_form': casa_form})


def Ver(request):
    casas = Casa.objects.all()

    return render(request, 'core/ver.html', context={'casas':casas})


def form_mod_vehiculo(request,id):
    casa = Casa.objects.get(direccion=id)

    datos ={
        'form': CasaForm(instance=casa)
    }
    if request.method == 'POST': 
        formulario = CasaForm(data=request.POST, instance = casa)
        if formulario.is_valid: 
            formulario.save()          
            return redirect('ver')
    return render(request, 'core/form_mod_vehiculo.html', datos)


def form_del_vehiculo(request,id):
    casa = Casa.objects.get(direccion=id)
    casa.delete()
    return redirect('ver')




'''serializers'''
from rest_framework.serializers import Serializer
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import CasaSerializer

@csrf_exempt
@api_view(['GET', 'POST'])



def lista_vehiculos(request): 
    if request.method== 'GET':
        casa = Casa.objects.all()
        serializer =CasaSerializer(casa, many=True)
        return Response(serializer.data)

    elif request.method=='POST': 
        data = JSONParser().parse(request)
        serializer = CasaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






   

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_vehiculo(request,id): 
    try: 
        casa = Casa.objects.get(casa=id) 
    except Casa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET': 
        serializer = CasaSerializer(casa)
        return Response(serializer.data)
    if request.method=='PUT': 
        data = JSONParser().parse(request)
        serializer = CasaSerializer(casa, data = data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE': 
        casa.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

def nosotros(request):
    return render(request, "nosotros.html")

def entrada(request):
    return render(request, "entrada.html")

def blog(request):
    return render(request, "blog.html")

def anuncios(request):
    return render(request, "anuncios.html")

def anuncio(request):
    return render(request, "anuncio.html")

def Contacto(request):
    return render(request, "contacto.html")

def login(request):
    return render(request, "login.html")
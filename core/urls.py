from django.urls import path
from .views import Contacto, anuncio, anuncios, blog, detalle_vehiculo, entrada, home, crearVehiculo,form_mod_vehiculo,Ver, form_del_vehiculo,nosotros,entrada,blog,anuncio,anuncios,Contacto,login

urlpatterns=[ 
    path('',home, name='home'),
    path('crear_vehiculo', crearVehiculo, name="crearVehiculo"),
    path('ver', Ver, name="ver"),
    path('form_mod_vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path('form_del_vehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"), 
    path('detalle_vehiculo/<id>', detalle_vehiculo, name="detalle_vehiculo"),
    path('nosotros', nosotros, name="Nosotros"),
    path('entrada', entrada, name="Entrada"),
    path('blog', blog, name="Blog"),
    path('anuncios', anuncios, name="Anuncios"),
    path('anuncio', anuncio, name="Anuncio"),
    path('contacto', Contacto, name="Contacto"),
    path('login', login, name="login"),
]


from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Casa, Categoria


class CasaForm(forms.ModelForm):

    class Meta: 
        model= Casa
        fields = ['direccion', 'comuna', 'ciudad', 'categoria']
        labels ={
            'direccion': 'Direccion', 
            'comuna': 'Comuna', 
            'ciudad': 'Ciudad', 
            'categoria': 'Categoría',
        }
        widgets={
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese casa', 
                    'id': 'direccion'
                }
            ), 
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese comuna', 
                    'id': 'comuna'
                }
            ), 
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ciudad', 
                    'id': 'ciudad'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

 
    
     


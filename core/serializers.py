from rest_framework import serializers
from .models import Casa

class CasaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Casa
        fields = ['direccion', 'comuna', 'ciudad', 'categoria']
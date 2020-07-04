from rest_framework import serializers
from .models import Tipo, Marca, Modelo, Auto

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer(many=False)
    class Meta:
        model = Modelo
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer(many=False)
    modelo = ModeloSerializer(many=False)
    class Meta:
        model = Auto
        fields = '__all__'
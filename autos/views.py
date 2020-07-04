from rest_framework import viewsets
from .serializers import TipoSerializer, MarcaSerializer, ModeloSerializer, AutoSerializer
from .models import Tipo, Marca, Modelo, Auto
from rest_framework import filters

class TipoView(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class MarcaView(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModeloView(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('modelo','marca__marca')

class AutoView(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('modelo__modelo','modelo__marca__marca')
    ordering_fields = ['anno', 'precio']
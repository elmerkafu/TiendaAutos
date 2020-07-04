<<<<<<< HEAD
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
=======
from django.shortcuts import render
from .forms import AutoForm, ModeloForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse

# Create your views here.


class InsertAuto(FormView):
    template_name = 'forms/auto.html'
    form_class = AutoForm
    success_url = reverse_lazy('admin:index')

    def form_valid(self, form):
        form.save()
        return super(InsertAuto, self).form_valid(form)

class InsertModelo(FormView):
    template_name = 'forms/modelo.html'
    form_class = ModeloForm
    success_url = reverse_lazy('admin:index')

    def form_valid(self, form):
        form.save()
        return super(InsertModelo, self).form_valid(form)

def login(request):
    return render(request, "forms/signIn.html", {})

def home(request):
    return render(request, "base.html", {})
>>>>>>> 3970c581f68cd81ffe5a3f5defb34dc336480211

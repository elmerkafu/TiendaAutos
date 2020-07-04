from django import forms
from .models import Auto, Tipo, Marca, Modelo


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ["tipo", "modelo", "auto", "anno", "precio", "foto"]

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ["tipo"]

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["marca"]

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ["marca", "modelo", "cilindros", "potencia",
        "sistema_alimentacion", "suspension_delantera", "suspension_posterior",
        "torque", "transmision", "frenos_delanteros", "frenos_traseros"
        ]

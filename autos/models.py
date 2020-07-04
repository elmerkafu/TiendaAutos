from django.db import models

# Create your models here.
class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50,blank=False, null=False)

    def __str__(self):
        return self.tipo

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=60,blank=False, null=False)

    def __str__(self):
        return self.marca

class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=60,blank=False, null=False)
    cilindros = models.CharField(max_length=60,blank=False, null=False)
    potencia = models.CharField(max_length=60,blank=False, null=False)
    sistema_alimentacion = models.CharField(max_length=60,blank=False, null=False)
    suspension_delantera = models.CharField(max_length=60,blank=False, null=False)
    suspension_posterior = models.CharField(max_length=60,blank=False, null=False)
    torque = models.CharField(max_length=60,blank=False, null=False)
    transmision = models.CharField(max_length=60,blank=False, null=False)
    frenos_delanteros = models.CharField(max_length=60,blank=False, null=False)
    frenos_traseros = models.CharField(max_length=60,blank=False, null=False)

    def __str__(self):
        return self.modelo

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    auto = models.CharField(max_length=60,blank=False, null=False)
    anno = models.IntegerField(blank=False, null=False)
    precio = models.FloatField(blank=False, null=False)
    foto = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.auto

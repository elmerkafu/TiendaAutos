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
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)
from .models import Datos
# Create your views here.b app cambios

class Lista(ListView):
    model = Datos

class Agregar(CreateView):
    model = Datos
    success_url = reverse_lazy('urls:lista')
    fields = ['nombre','descripcion','inicio','fin','image']

class Actualiza(UpdateView):
    model = Datos
    success_url = reverse_lazy('urls:lista')
    fields = ['nombre','descripcion','inicio','fin','image']

class Detalle(DetailView):
    model = Datos

class Borrar(DeleteView):
    model = Datos
    success_url = reverse_lazy('urls:lista')
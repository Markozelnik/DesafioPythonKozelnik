from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

# *
# * Inicio
# *


# def index(request: HttpRequest) -> HttpResponse:
#     return render(request, "producto/index.html")

class  ProductoCategoriaList (models.Model):
    nombre = models.CharField (max_lenght=50)
    
    def __str__(self):
        return self.nombre


class IndexView(TemplateView):
    template_name = "producto/index.html"




class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

    def get_queryset(self):
        """Devuelve los productos de la categoria escrita por el usuario en el formulario de búsqueda"""
        # Si la búsqueda tiene algún texto introducido, devuelve todos los productos que contengan dicho texto
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=query)
        # Si no, devuelve todos los productos
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:index")



class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")



class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    form_class = forms.ProductoCategoriaForm



def producto_categoria_detail(request: HttpRequest, pk) -> HttpResponse:
    categoria = models.ProductoCategoria.objects.get(id=pk)
    return render(request, "merch.html", {"object": categoria})


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    



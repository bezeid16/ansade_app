# ansade_app/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product, ProductFamily
from django.urls import reverse_lazy

def home(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

def list(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product  

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductFamilyList(ListView):
    model = ProductFamily

class ProductFamilyDetail(DetailView):
    model = ProductFamily

class ProductFamilyCreate(CreateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('product_family_list')

class ProductFamilyDelete(DeleteView):
    model = ProductFamily
    success_url = reverse_lazy('product_family_list')

class ProductFamilyUpdate(UpdateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('product_family_list')

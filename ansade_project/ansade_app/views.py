# ansade_app/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import FamilleProduit, Produit, Panier, PanierProduit, Price, PointDeVente

from django.shortcuts import render

def home(request):

    return render(request, 'ansade_app/home.html')

# FamilleProduit Views
class FamilleProduitListView(ListView):
    model = FamilleProduit

class FamilleProduitDetailView(DetailView):
    model = FamilleProduit

class FamilleProduitCreateView(CreateView):
    model = FamilleProduit
    fields = '__all__'
    success_url = reverse_lazy('famille_produit_list')  # Redirect to the list view after creating

class FamilleProduitUpdateView(UpdateView):
    model = FamilleProduit
    fields = '__all__'
    success_url = reverse_lazy('famille_produit_list')  # Redirect to the list view after updating

class FamilleProduitDeleteView(DeleteView):
    model = FamilleProduit
    success_url = reverse_lazy('famille_produit_list')  # Redirect to the list view after deleting

# Produit Views
class ProduitListView(ListView):
    model = Produit

class ProduitDetailView(DetailView):
    model = Produit

class ProduitCreateView(CreateView):
    model = Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')  # Redirect to the list view after creating

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')  # Redirect to the list view after updating

class ProduitDeleteView(DeleteView):
    model = Produit
    success_url = reverse_lazy('produit_list')  # Redirect to the list view after deleting

# Panier Views
class PanierListView(ListView):
    model = Panier

class PanierDetailView(DetailView):
    model = Panier

class PanierCreateView(CreateView):
    model = Panier
    fields = '__all__'
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after creating

class PanierUpdateView(UpdateView):
    model = Panier
    fields = '__all__'
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after updating

class PanierDeleteView(DeleteView):
    model = Panier
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after deleting



class PanierProduitListView(ListView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_list.html'  # Specify the template name

class PanierProduitDetailView(DetailView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_detail.html'  # Specify the template name

class PanierProduitCreateView(CreateView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_form.html'  # Specify the template name
    fields = '__all__'
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after creating

class PanierProduitUpdateView(UpdateView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_form.html'  # Specify the template name
    fields = '__all__'
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after updating

class PanierProduitDeleteView(DeleteView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_confirm_delete.html'  # Specify the template name
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after deleting


# Price Views
class PriceListView(ListView):
    model = Price

class PriceDetailView(DetailView):
    model = Price

class PriceCreateView(CreateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')  # Redirect to the list view after creating

class PriceUpdateView(UpdateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')  # Redirect to the list view after updating

class PriceDeleteView(DeleteView):
    model = Price
    success_url = reverse_lazy('price_list')  # Redirect to the list view after deleting

# PointDeVente Views
class PointDeVenteListView(ListView):
    model = PointDeVente

class PointDeVenteDetailView(DetailView):
    model = PointDeVente

class PointDeVenteCreateView(CreateView):
    model = PointDeVente
    fields = ['code', 'wilaya', 'moughtaa', 'commune', 'gps_lat', 'gps_long']
    success_url = reverse_lazy('point_de_vente_list')  # Redirect to the list view after creating

class PointDeVenteUpdateView(UpdateView):
    model = PointDeVente
    fields = ['code', 'wilaya', 'moughtaa', 'commune', 'gps_lat', 'gps_long']
    success_url = reverse_lazy('point_de_vente_list')  # Redirect to the list view after updating

class PointDeVenteDeleteView(DeleteView):
    model = PointDeVente
    fields = ['code', 'wilaya', 'moughtaa', 'commune', 'gps_lat', 'gps_long']
    success_url = reverse_lazy('point_de_vente_list')  # Redirect to the list view after deleting

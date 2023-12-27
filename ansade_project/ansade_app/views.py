# ansade_app/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import FamilleProduit, Produit, Panier, PanierProduit, Price, PointDeVente

# FamilleProduit Views
class FamilleProduitListView(ListView):
    model = FamilleProduit

class FamilleProduitDetailView(DetailView):
    model = FamilleProduit

class FamilleProduitCreateView(CreateView):
    model = FamilleProduit
    fields = ['label']
    success_url = reverse_lazy('famille_produit_list')  # Redirect to the list view after creating

class FamilleProduitUpdateView(UpdateView):
    model = FamilleProduit
    fields = ['label']
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
    fields = ['label', 'price_unit', 'code', 'famille_produit']
    success_url = reverse_lazy('produit_list')  # Redirect to the list view after creating

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = ['label', 'price_unit', 'code', 'famille_produit']
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
    fields = ['label', 'code', 'description']
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after creating

class PanierUpdateView(UpdateView):
    model = Panier
    fields = ['label', 'code', 'description']
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after updating

class PanierDeleteView(DeleteView):
    model = Panier
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after deleting

# PanierProduit Views
class PanierProduitCreateView(CreateView):
    model = PanierProduit
    fields = ['price', 'panier', 'ponderation']
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after creating

class PanierProduitUpdateView(UpdateView):
    model = PanierProduit
    fields = ['price', 'panier', 'ponderation']
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after updating

class PanierProduitDeleteView(DeleteView):
    model = PanierProduit
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after deleting

# Price Views
class PriceCreateView(CreateView):
    model = Price
    fields = ['value', 'date', 'point_de_vente', 'produit']
    success_url = reverse_lazy('price_list')  # Redirect to the list view after creating

class PriceUpdateView(UpdateView):
    model = Price
    fields = ['value', 'date', 'point_de_vente', 'produit']
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
    success_url = reverse_lazy('point_de_vente_list')  # Redirect to the list view after deleting

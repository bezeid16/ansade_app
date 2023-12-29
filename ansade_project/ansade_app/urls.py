# ansade_app/urls.py
from . import views

from django.urls import path
from .views import (
    FamilleProduitListView, FamilleProduitDetailView, FamilleProduitCreateView, FamilleProduitUpdateView, FamilleProduitDeleteView,
    ProduitListView, ProduitDetailView, ProduitCreateView, ProduitUpdateView, ProduitDeleteView,
    PanierListView, PanierDetailView, PanierCreateView, PanierUpdateView, PanierDeleteView,
    PanierProduitListView,PanierProduitDetailView,
    PanierProduitCreateView, PanierProduitUpdateView, PanierProduitDeleteView,
    PriceListView,PriceDetailView,
    PriceCreateView, PriceUpdateView, PriceDeleteView,
    PointDeVenteListView, PointDeVenteDetailView, PointDeVenteCreateView, PointDeVenteUpdateView, PointDeVenteDeleteView,
)

urlpatterns = [

    path('', views.home, name='home'),



    # FamilleProduit URLs
    path('familles/', FamilleProduitListView.as_view(), name='famille_produit_list'),
    path('familles/<int:pk>/', FamilleProduitDetailView.as_view(), name='famille_produit_detail'),
    path('familles/create/', FamilleProduitCreateView.as_view(), name='famille_produit_create'),
    path('familles/<int:pk>/update/', FamilleProduitUpdateView.as_view(), name='famille_produit_update'),
    path('familles/<int:pk>/delete/', FamilleProduitDeleteView.as_view(), name='famille_produit_delete'),

    # Produit URLs
    path('produits/', ProduitListView.as_view(), name='produit_list'),
    path('produits/<int:pk>/', ProduitDetailView.as_view(), name='produit_detail'),
    path('produits/create/', ProduitCreateView.as_view(), name='produit_create'),
    path('produits/<int:pk>/update/', ProduitUpdateView.as_view(), name='produit_update'),
    path('produits/<int:pk>/delete/', ProduitDeleteView.as_view(), name='produit_delete'),

    # Panier URLs
    path('paniers/', PanierListView.as_view(), name='panier_list'),
    path('paniers/<int:pk>/', PanierDetailView.as_view(), name='panier_detail'),
    path('paniers/create/', PanierCreateView.as_view(), name='panier_create'),
    path('paniers/<int:pk>/update/', PanierUpdateView.as_view(), name='panier_update'),
    path('paniers/<int:pk>/delete/', PanierDeleteView.as_view(), name='panier_delete'),

    # PanierProduit URLs
    path('panierproduits/', PanierProduitListView.as_view(), name='panier_produit_list'),
    path('panierproduits/<int:pk>/', PanierProduitDetailView.as_view(), name='panier_produit_detail'),
    path('panierproduits/create/', PanierProduitCreateView.as_view(), name='panier_produit_create'),
    path('panierproduits/<int:pk>/update/', PanierProduitUpdateView.as_view(), name='panier_produit_update'),
    path('panierproduits/<int:pk>/delete/', PanierProduitDeleteView.as_view(), name='panier_produit_delete'),

    # Price URLs
    path('prices/', PriceListView.as_view(), name='price_list'),
    path('prices/<int:pk>/', PriceDetailView.as_view(), name='price_detail'),
    path('prices/create/', PriceCreateView.as_view(), name='price_create'),
    path('prices/<int:pk>/update/', PriceUpdateView.as_view(), name='price_update'),
    path('prices/<int:pk>/delete/', PriceDeleteView.as_view(), name='price_delete'),

    # PointDeVente URLs
    path('points/', PointDeVenteListView.as_view(), name='point_de_vente_list'),
    path('points/<int:pk>/', PointDeVenteDetailView.as_view(), name='point_de_vente_detail'),
    path('points/create/', PointDeVenteCreateView.as_view(), name='point_de_vente_create'),
    path('points/<int:pk>/update/', PointDeVenteUpdateView.as_view(), name='point_de_vente_update'),
    path('points/<int:pk>/delete/', PointDeVenteDeleteView.as_view(), name='point_de_vente_delete'),
]

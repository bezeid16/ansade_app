# ansade_app/resources.py
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import FamilleProduit, Produit, Panier, PanierProduit, Price, PointDeVente

class FamilleProduitResource(resources.ModelResource):
    class Meta:
        model = FamilleProduit
        fields = ('id', 'label')

class ProduitResource(resources.ModelResource):
    famille_produit = Field(
        column_name='famille_produit',
        attribute='famille_produit',
        widget=ForeignKeyWidget(FamilleProduit, 'label')
    )

    class Meta:
        model = Produit
        fields = ('id', 'label', 'price_unit', 'code', 'famille_produit__label')

class PanierResource(resources.ModelResource):
    class Meta:
        model = Panier
        fields = ('id', 'label', 'code', 'description')

class PanierProduitResource(resources.ModelResource):
    price = Field(
        column_name='price',
        attribute='price',
        widget=ForeignKeyWidget(Price, 'value')
    )

    panier = Field(
        column_name='panier',
        attribute='panier',
        widget=ForeignKeyWidget(Panier, 'label')
    )

    class Meta:
        model = PanierProduit
        fields = ('id', 'price__value', 'panier__label', 'ponderation')

class PriceResource(resources.ModelResource):
    point_de_vente = Field(
        column_name='point_de_vente',
        attribute='point_de_vente',
        widget=ForeignKeyWidget(PointDeVente, 'code')
    )

    produit = Field(
        column_name='produit',
        attribute='produit',
        widget=ForeignKeyWidget(Produit, 'label')
    )

    class Meta:
        model = Price
        fields = ('id', 'value', 'date', 'point_de_vente__code', 'produit__label')

class PointDeVenteResource(resources.ModelResource):
    class Meta:
        model = PointDeVente
        fields = ('id', 'code', 'wilaya', 'moughtaa', 'commune', 'gps_lat', 'gps_long')

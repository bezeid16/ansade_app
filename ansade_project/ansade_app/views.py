# ansade_app/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import FamilleProduit, Produit, Panier, PanierProduit, Price, PointDeVente, PriceIndex
from django.shortcuts import render, get_object_or_404
from .resources import FamilleProduitResource, ProduitResource ,PanierResource ,PanierProduitResource ,PriceResource ,PointDeVenteResource # Importez d'autres ressources nécessaires
from django.http import HttpResponse
from tablib import Dataset
from django.contrib import messages
from django.shortcuts import redirect
import csv
from django.views.generic import TemplateView




def ipc_view(request):
    try:
        # Essayez de récupérer l'objet PriceIndex, sinon lancez une exception
        price_index = PriceIndex.objects.get()  # Ajoutez les filtres nécessaires ici
    except PriceIndex.DoesNotExist:
        # Si l'objet n'existe pas, renvoyez une page avec un message approprié
        return render(request, 'ansade_app/priceindex_not_found.html')

    # Si l'objet est trouvé, continuez avec le traitement normal
    return render(request, 'ansade_app/ipc.html', {'price_index': price_index})









class ProductPriceChart(TemplateView):
    template_name = 'product_price_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['product_id']
        prices = Price.objects.filter(produit_id=product_id).order_by('date')
        context['product_id'] = product_id
        context['labels'] = [price.date.strftime('%Y-%m-%d') for price in prices]
        context['values'] = [price.value for price in prices]
        return context
#famille produit
def export_famille_produit(request):
    famille_produit_resource = FamilleProduitResource()
    dataset = famille_produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="famille_produit.csv"'
    return response

def import_famille_produit(request):
    result_message = None

    if request.method == 'POST':
        famille_produit_resource = FamilleProduitResource()
        dataset = Dataset()
        new_famille_produit_file = request.FILES['myfile']

        if not new_famille_produit_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_famille_produit_file.read().decode('utf-8'))
                famille_produit_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#produit
def export_produit(request):
    produit_resource = ProduitResource()
    dataset = produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="produit.csv"'
    return response

def import_produit(request):
    result_message = None

    if request.method == 'POST':
        produit_resource = ProduitResource()
        dataset = Dataset()
        new_produit_file = request.FILES['myfile']

        if not new_produit_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_produit_file.read().decode('utf-8'))
                produit_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#Panier
def export_Panier(request):
    Panier_resource = PanierResource()
    dataset = Panier_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Panier.csv"'
    return response

def import_Panier(request):
    result_message = None

    if request.method == 'POST':
        Panier_resource = PanierResource()
        dataset = Dataset()
        new_Panier_file = request.FILES['myfile']

        if not new_Panier_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_Panier_file.read().decode('utf-8'))
                Panier_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#PanierProduit
def export_PanierProduit(request):
    PanierProduit_resource = PanierProduitResource()
    dataset = PanierProduit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="PanierProduit.csv"'
    return response

def import_PanierProduit(request):
    result_message = None

    if request.method == 'POST':
        PanierProduit_resource = PanierProduitResource()
        dataset = Dataset()
        new_PanierProduit_file = request.FILES['myfile']

        if not new_PanierProduit_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_PanierProduit_file.read().decode('utf-8'))
                PanierProduit_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#Price
def export_Price(request):
    Price_resource = PriceResource()
    dataset = Price_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Price.csv"'
    return response

def import_Price(request):
    result_message = None

    if request.method == 'POST':
        price_resource = PriceResource()
        dataset = Dataset()
        new_price_file = request.FILES['myfile']

        if not new_price_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_price_file.read().decode('utf-8'))
                price_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#PointDeVente
def export_PointDeVente(request):
    PointDeVente_resource = PointDeVenteResource()
    dataset = PointDeVente_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="PointDeVente.csv"'
    return response

def import_PointDeVente(request):
    result_message = None

    if request.method == 'POST':
        PointDeVente_resource = PointDeVenteResource()
        dataset = Dataset()
        new_PointDeVente_file = request.FILES['myfile']

        if not new_PointDeVente_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_PointDeVente_file.read().decode('utf-8'))
                PointDeVente_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})


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


def famille_produit_search(request):
    search_query = request.GET.get('search_query', '')
    famille_produits = FamilleProduit.objects.filter(label__icontains=search_query)

    context = {'famille_produits': famille_produits, 'search_query': search_query}
    return render(request, 'familleproduit_list.html', context)
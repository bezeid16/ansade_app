# ansade_app/urls.py

from django.urls import path
from .views import home, ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete, ProductFamilyList, ProductFamilyDetail, ProductFamilyCreate, ProductFamilyUpdate, ProductFamilyDelete

urlpatterns = [
    path('', home, name='home'),

    # URLs pour les produits (Product)
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('products/create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),

    # URLs pour les familles de produits (ProductFamily)
    path('families/', ProductFamilyList.as_view(), name='product_family_list'),
    path('families/<int:pk>/', ProductFamilyDetail.as_view(), name='product_family_detail'),
    path('families/create/', ProductFamilyCreate.as_view(), name='product_family_create'),
    path('families/<int:pk>/update/', ProductFamilyUpdate.as_view(), name='product_family_update'),
    path('families/<int:pk>/delete/', ProductFamilyDelete.as_view(), name='product_family_delete'),
]

from django.urls import path
from .views import index , CreateProduct, UpdateProduct, DeleteProduct

app_name = 'produits'
urlpatterns = [
    #'' <- racine du projet , index: ma vue
    #à la racine du projet , appelle-moi l'index et le nom de cet index est index
    path('', index, name='index'),
    path('create-produit/', CreateProduct.as_view(), name='create_product'),
    path('produitUpdate/<int:pk>/', UpdateProduct.as_view(), name='produitUpdate'),
    
    path('produitDelete/<int:pk>/', DeleteProduct.as_view(), name='produitDelete'),



]

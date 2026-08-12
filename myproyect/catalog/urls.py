from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # Ruta principal -> Landing Page
    path('', views.index, name='index'),
    
    # Ruta del catálogo -> Lista de productos
    path('catalogo/', views.product_list, name='product_list'),
    
    # Detalle de producto
    path('producto/<str:pk>/', views.product_detail, name='product_detail'),
]
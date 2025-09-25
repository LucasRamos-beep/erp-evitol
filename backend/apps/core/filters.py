# apps/core/filters.py

from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    # Permite filtrar por um preço mínimo (maior ou igual a 'gte')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')

    # Permite filtrar por um preço máximo (menor ou igual a 'lte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    # Permite buscar por parte do nome, ignorando maiúsculas/minúsculas
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        # Adicionamos os novos filtros à lista de campos
        fields = ['name', 'min_price', 'max_price']
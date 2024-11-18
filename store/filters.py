import django_filters
from .models import Product
from django_filters.rest_framework import FilterSet

# Define the ProductFilter class
class ProductFilter(FilterSet):
    inventory = django_filters.NumberFilter(field_name='inventory', lookup_expr='lt')  # Filter for inventory less than a specified value

    class Meta:
        model = Product
        fields = ['inventory']  # Only filter the inventory field

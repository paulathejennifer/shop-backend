from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'your_template.html', {'products': products})

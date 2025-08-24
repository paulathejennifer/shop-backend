from django.urls import path, include
from .views import list_products


urlPatterns=[
    path('products/','list_products', name = 'product_list'),
    path('catalogue', include('catalogue.urls'))

]
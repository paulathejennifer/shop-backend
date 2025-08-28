from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_products(request):
    return redirect('catalogue:product_list')  


urlpatterns = [
    path('', redirect_to_products),         
    path('catalogue/', include('catalogue.urls')),
]

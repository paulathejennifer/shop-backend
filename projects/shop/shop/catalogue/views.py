from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.views.decorators.http import require_POST

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalogue/product_list.html', {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalogue/product_detail.html', {"product": product})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue:product_list") 
    else:
        form = ProductForm()
    return render(request, 'catalogue/product_form.html', {"form": form})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1  
    request.session['cart'] = cart
    return redirect('catalogue:cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total_price = 0
    for product in products:
        quantity = cart.get(str(product.id), 0)
        total = product.price * quantity
        total_price += total
        cart_items.append({'product': product, 'quantity': quantity, 'total': total})
    return render(request, 'catalogue/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
    return redirect('catalogue:cart_detail')

@require_POST
def update_cart_quantity(request, product_id):
    cart = request.session.get('cart', {})
    change = int(request.POST.get('quantity_change', 0))
    product_id_str = str(product_id)
    if product_id_str in cart:
        new_quantity = cart[product_id_str] + change
        if new_quantity > 0:
            cart[product_id_str] = new_quantity
        else:
            cart.pop(product_id_str)
        request.session['cart'] = cart
    return redirect('catalogue:cart_detail')

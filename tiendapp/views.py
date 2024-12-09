from django.shortcuts import render
from tiendapp.models import Product, ProductCategory


# Create your views here.
def v_index(request):
    product_db = Product.objects.all()
    
    context = {
        #"products": [None, None, None, None, None]
        'products': product_db
    }
    return render(request, "tiendapp/index.html", context)

def v_cart(request):
    context = {
        "items": [None, None, None, None, None]
    }
    return render(request, "tiendapp/cart.html", context)

def v_product_detail(request, code):
    product_obj = Product.objects.get(sku = code)
    # Obtejer las categorias del producto
    categories_obj = ProductCategory.objects.filter(product = product_obj) # lista de categorias
    # De las categorias obtenidas
    # Filtrar los productos relacionados
    pc_obj = ProductCategory.objects.filter(category__in = categories_obj)
    extras = []
    for pc in pc_obj:
        extras.append(pc.product)
    context = {
        'product': product_obj,
        "extras": extras
    }
    return render(request, "tiendapp/product_detail.html", context)

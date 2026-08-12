from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product

# --- ESTA ES LA FUNCIÓN QUE FALTA ---
def index(request):
    return render(request, 'catalog/index.html')
# ------------------------------------

@login_required
def product_list(request):
    query = request.GET.get('q','')
    
    if query:
        product_list = Product.objects.filter(
            Q(item__icontains=query) |
            Q(title__icontains=query) |
            Q(area__icontains=query)
        ).order_by('-created_at')
    else:
        product_list = Product.objects.all().order_by('-created_at')
        
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'catalog/product_list.html', {
        'products': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'query': query
    })
    
@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
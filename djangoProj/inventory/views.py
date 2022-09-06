from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Supermarket, Product, Stock

# Create your views here.
def index(request):
    supermarkets_list = Supermarket.objects.values()
    context = {
        'supermarkets_list': supermarkets_list,
    }
    return render(request, 'inventory/index.html', context)

def supDetail(request, supermarket_id):
    supermarket = get_object_or_404(Supermarket, pk=supermarket_id)
    return render(request, 'inventory/singleSupermarket.html', {'supermarket_data': supermarket})

def supStock(request, supermarket_id):
    supermarket = get_object_or_404(Supermarket, pk=supermarket_id)
    stock_list = Stock.objects.filter(supermarket_id=supermarket_id).select_related()
    context = {
        'stock_list': stock_list,
        'supermarket': supermarket
    }
    return render(request, 'inventory/supermarketStock.html', context)

def checkOut(request, stockItem_id):
    stock = get_object_or_404(Stock, pk=stockItem_id).select_related()
    stock.number_in_stock -= 1
    stock.save()
    return HttpResponseRedirect(reverse('inventory/supermarketStock.html', args=(stock.product_id)))


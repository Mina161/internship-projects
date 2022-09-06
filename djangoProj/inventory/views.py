from decimal import setcontext
from itertools import product
from multiprocessing import get_context
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.views import generic
from .models import Supermarket, Product, Stock, Brand

def checkOut(request, stockItem_id):
    stock = get_object_or_404(Stock, pk=stockItem_id)
    stock.number_in_stock -= 1
    if(stock.number_in_stock == 0):
        stock.delete()
    else:
        stock.save()
    return HttpResponseRedirect(reverse('inventory:SupermarketStock', args=(stock.supermarket_id,)))

def addStock(request, supermarket_id):
    try:
        s = Stock(supermarket_id = supermarket_id, product_id = request.POST['product_id'], expiry_date = request.POST['expiry_date'], number_in_stock = request.POST['number_in_stock'])
        s.save()
    except:
        context = {
            'pk': supermarket_id,
            'supermarket': Supermarket.objects.get(id = supermarket_id),
            'stock_list': Stock.objects.filter(supermarket_id = supermarket_id).select_related(),
            'product_list': Product.objects.all(),
            'errorMessage': "Invalid Form Submission",
        }
        return render(request, 'inventory/supermarketStock.html', context)
    else:
        return HttpResponseRedirect(reverse('inventory:SupermarketStock', args=(supermarket_id,)))

class IndexView(generic.TemplateView):
    template_name = 'inventory/index.html'
class SupermarketIndexView(generic.ListView):
    template_name = 'inventory/supermarketIndex.html'
    context_object_name = 'supermarkets_list'

    def get_queryset(self):
        return Supermarket.objects.values()

class ProductIndexView(generic.ListView):
    template_name = 'inventory/productIndex.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.select_related()


class SupermarketDetailView(generic.DetailView):
    model = Supermarket
    template_name = 'inventory/singleSupermarket.html'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'inventory/productDetail.html'

class StockView(generic.ListView):
    template_name = 'inventory/supermarketStock.html'
    context_object_name = 'stock_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supermarket'] = Supermarket.objects.get(id = self.kwargs['pk'])
        context['product_list'] = Product.objects.all()
        print(self.args)
        return context
    def get_queryset(self):
        return Stock.objects.filter(supermarket_id = self.kwargs['pk']).select_related()

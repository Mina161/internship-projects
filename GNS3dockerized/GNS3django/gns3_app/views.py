from django.shortcuts import render
from netmiko import ConnectHandler
from .models import Router
from decimal import setcontext
from multiprocessing import get_context
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.views import generic
from .forms import RouterForm

# Create your views here.
from django.http import HttpResponse

class IndexView(generic.TemplateView):
    template_name = 'gns3_app/index.html'

def addRouter(request):
    try:
        r = Router(device_type = "cisco_ios", name = request.POST['name'], ip = request.POST['ip'], username = request.POST['username'], password = request.POST['password'], secret = request.POST['secret'])
        r.save()
    except:
        context = {
            'errorMessage': "Invalid Form Submission",
        }
        return render(request, 'inventory/supermarketStock.html', context)
    else:
        return HttpResponseRedirect(reverse('inventory:SupermarketStock', args=(supermarket_id,)))
    
class RouterListView(generic.ListView):
    template_name = 'gns3_app/RouterIndex.html'
    model = Router

class RouterDetailView(generic.DetailView):
    template_name = 'gns3_app/RouterDetail.html'
    model = Router
    context_object_name = 'router_details'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        R = Router.objects.get(id = self.kwargs['pk'])
        context['ip_brief'] = connect_ssh(R)
        context['router'] = R
        return context

def addRouter(request):
    if request.method == 'POST':
        form = RouterForm(request.POST)
        if form.is_valid():
            r = Router(device_type = "cisco_ios", name = request.POST['name'], host = request.POST['host'], username = request.POST['username'], password = request.POST['password'], secret = request.POST['secret'], port = request.POST['port'])
            r.save()
            return HttpResponseRedirect(reverse('gns3_app:routerIndex'))
    else:
        form = RouterForm()

    return render(request, 'gns3_app/routerForm.html', {'form': form})

def connect_ssh(R):
    cisco_router = {
        'device_type': R.device_type,
        'host': R.host,
        'username': R.username,
        'password': R.password,
        'secret': R.secret,
        'port': R.port,
    }
    
    ssh = ConnectHandler(**cisco_router)
    result = ssh.send_command('show ip int br')
    
    return result
from django.shortcuts import render
from netmiko import ConnectHandler

R_1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.2',
    'username': 'cisco',
    'password': 'cisco',
}

# Create your views here.
from django.http import HttpResponse

def home(request):
    net_connect = ConnectHandler(**R_1)
    output = net_connect.send_command('show ip int brief')
    return HttpResponse(output)
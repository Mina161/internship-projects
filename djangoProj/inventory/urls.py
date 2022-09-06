from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
    path('supermarket', views.index, name='index'),
    path('supermarket/<int:supermarket_id>/', views.supDetail, name='SupermarketDetail'),
    path('supermarket/<int:supermarket_id>/stock', views.supStock, name='SupermarketStock'),
    path('supermarket/<int:supermarket_id>/stock/checkOut/<int:stockItem_id>', views.checkOut, name='checkOut'),
]
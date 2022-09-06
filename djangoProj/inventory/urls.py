from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('supermarket', views.IndexView.as_view(), name='index'),
    path('supermarket/<int:pk>/', views.SupermarketDetailView.as_view(), name='SupermarketDetail'),
    path('supermarket/<int:pk>/stock', views.StockView.as_view(), name='SupermarketStock'),
    path('supermarket/checkout/<int:stockItem_id>', views.checkOut, name='checkOut'),
    path('supermarket/add/<int:supermarket_id>', views.addStock, name='addStock'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='ProductDetail'),
]
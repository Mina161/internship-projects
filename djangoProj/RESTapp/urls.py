from django.urls import path
from RESTapp import views

app_name = 'cars'
urlpatterns = [
    path('', views.car_list),
    path('<int:pk>/', views.car_detail),
]
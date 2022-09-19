from django.urls import path
from gns3_app import views

urlpatterns = [
    path("", views.home, name="home"),
]
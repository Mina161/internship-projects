from django.urls import path
from gns3_app import views

app_name = 'gns3_app'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("routers", views.RouterListView.as_view(), name="routerIndex"),
    path("routers/<int:pk>", views.RouterDetailView.as_view(), name="routerDetail"),
    path("routers/add",views.addRouter, name="routerForm")
]
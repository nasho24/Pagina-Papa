from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<slug:slug>/', views.categoria_detalle, name='categoria_detalle'),
]
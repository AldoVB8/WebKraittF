from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-aldo'),
    path('pages-aldo.html', views.pages, name='pages-aldo'),
    path('contact/', views.contact, name='contact-aldo'),
    path('services/', views.services, name='services-aldo'),
    path('nosotros/', views.nosotros, name='nosotros-aldo'),
    path('<slug:slug>.html', views.product_detail, name='product_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Blog IA
    path('ia/', views.blog_index_ia, name='blog_index-aldo'),
    path('ia/recurso/<int:pk>/', views.resource_detail, name='resource_detail-aldo'),

    # Rutas para Blog General
    path('blog/', views.blog_general_index, name='blog_general_index'),
    path('blog/<slug:slug>/', views.blog_general_detail, name='blog_general_detail'),
]

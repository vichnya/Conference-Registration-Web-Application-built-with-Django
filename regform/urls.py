from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.index_2, name='index_2'),
    path('about/create', views.create, name='create'),
    
]
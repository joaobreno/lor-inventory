from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('<int:card_id>', views.card, name='card'),
    path('search', views.search, name='search'),
    path('filter_page', views.filter_page, name='filter_page'),
    path('collection', views.collection, name='collection')

]

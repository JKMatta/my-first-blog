from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.post_list, name='post_list'),
    path('photos', views.galery, name='galery'),
]
from django.urls import path
from . import views

#map our index function to the root of our notebook app 
urlpatterns = [
    path('', views.index, name='index')
]
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('/trends', views.trends, name='trends'),
    path('/about', views.about, name='about'),
    # path('', views., name=''),
    # path('', views., name=''),
]

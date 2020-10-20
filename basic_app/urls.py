from django.urls import path
from . import views

# TEMPLATE TAGGING

# app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relatives'),
    path('other/', views.other, name='others'),
    path('', views.index, name='index')
]



from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('allocations/', views.AllocationList.as_view(), name='allocation-list'),
    path('allocations/<pk>/', views.AllocationDetail.as_view(), name='allocation-detail'),
    path('provinces', views.ProvinceList.as_view(), name='province-list'),
    path('provinces/<pk>/', views.ProvinceDetail.as_view(), name='province-detail'),
]

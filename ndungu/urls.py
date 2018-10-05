from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('allocations/', views.AllocationList.as_view(), name='allocation-list'),
    path('allocations/<pk>/', views.AllocationDetail.as_view(), name='allocation-detail'),
    path('provinces/', views.ProvinceList.as_view(), name='province-list'),
    path('provinces/<pk>/', views.ProvinceDetail.as_view(), name='province-detail'),
    path('municipalities/', views.MunicipalityList.as_view(), name='municipality-list'),
    path('municipalities/<pk>/', views.MunicipalityDetail.as_view(), name='municipality-detail'),
    path('authorities/', views.AuthorityList.as_view(), name='authority-list'),
    path('authorities/<pk>/', views.AuthorityDetail.as_view(), name='authority-detail'),
    path('entities/', views.EntityList.as_view(), name='entity-list'),
    path('entities/<pk>/', views.EntityDetail.as_view(), name='entity-detail'),
]

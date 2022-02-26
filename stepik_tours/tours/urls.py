from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('departure/<str:departure>', views.departure_view, name='departure-view'),
    path('tour/<int:id>/', views.tour_view, name='tour-view'),
]

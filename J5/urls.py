from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.jfivehomepage, name="jfivehomepage"),
    path('addsubmission', views.addsubmission, name="jfive_addsubmission"),
    path('strategies', views.strategies, name="jfive_strategies"),
    path('final/', views.final, name="final"),
]

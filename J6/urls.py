from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.jsixhomepage, name="jsixhomepage"),
    path('addsubmission', views.j6addsubmission, name="jsix_addsubmission"),
    path('comm', views.comm, name="jsix_comm"),
    path('final/', views.final, name="final"),
]

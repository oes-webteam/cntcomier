from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.jsevenhomepage, name="jsevenhomepage"),
    path('addsubmission', views.j7addsubmission, name="jseven_addsubmission"),
    path('training', views.training, name="jseven_training"),
    path('final/', views.final, name="final"),
]

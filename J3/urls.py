from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.jthreehomepage, name="jthreehomepage"),
    path('addsubmission', views.addsubmission, name="jthree_addsubmission"),
    path('ops', views.ops, name="jthree_ops"),
    path('final/', views.final, name="final"),
]

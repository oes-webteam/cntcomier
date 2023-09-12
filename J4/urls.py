from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.jfourhomepage, name="jfourhomepage"),
    path('addsubmission', views.addsubmission, name="jfour_addsubmission"),
    path('logistic', views.logistic, name="jfour_logistic"),
    path('final/', views.final, name="final"),
]

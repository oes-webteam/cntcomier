from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.jonehomepage, name="jonehomepage"),
    path('addsubmission', views.addsubmission, name="jone_addsubmission"),
    path('humanresources', views.humanresources, name="jone_humanceresources"),
    path('final/', views.final, name="final"),
]

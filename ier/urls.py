from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('steps/<int:step>', views.FormView, name='steps'),
    path('', views.homepage_view, name="home"),
    path('final/', views.final, name="final"),
]

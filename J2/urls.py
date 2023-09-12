from django.contrib import admin
from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.jtwohomepage, name='jtwohomepage'),
#     path('addsubmission', views.addsubmission, name='jtwo_addsubmission'),
#     path('intell', views.intell, name='jtwo_intell'),
#     path('final/', views.final, name='final')
# ]
urlpatterns = [
    path('', views.jtwohomepage, name="jtwohomepage"),
    path('addsubmission', views.addsubmission, name="jtwo_addsubmission"),
    path('intell', views.intell, name="jtwo_intell"),
    path('final/', views.final, name="final"),
]

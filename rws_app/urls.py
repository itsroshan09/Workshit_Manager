# rws_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work/add/', views.add_work, name='add_work'),
    path('work/<int:work_id>/add-bill/', views.add_bill, name='add_bill'),
]
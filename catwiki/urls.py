from django.urls import path

from . import views

app_name = 'catwiki'

urlpatterns = [
    path('', views.index, name='index'),
    path('searched', views.most_searched, name='searched'),
    path('detail/<str:breed_id>/', views.details_breed, name='detail'),
]

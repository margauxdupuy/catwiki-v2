from django.urls import path
from catwiki_web import views

app_name = 'catwiki_web'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('searched', views.SearchedView.as_view(), name='searched'),
    path('why-you-should-have-a-cat', views.WhyCatView.as_view(), name='why-cat'),
    path('detail/<str:id_name>/', views.DetailView.as_view(), name='detail'),
    path('data-catapi', views.FetchDataCatAPIView.as_view(), name='catapi')
]

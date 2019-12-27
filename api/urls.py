from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
   # path('', views.search,name='search'),
    path('api/search',views.search,name='api_app_search'),
    path('api/details', views.details, name='api_app_details'),
]

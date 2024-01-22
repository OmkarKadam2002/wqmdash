from django.contrib import admin
from django.urls import path
from wqmIOT import views
urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/get_latest_sensor_data/', views.get_latest_sensor_data, name='get_latest_sensor_data'),
    path('aboutproject/', views.about_project, name='about_project'),
]

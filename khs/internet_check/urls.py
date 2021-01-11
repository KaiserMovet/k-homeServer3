from django.urls import path

from . import views

app_name = 'internet_check'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/internet_speed', views.api_internet_speed),
    path('api/internet_status', views.api_internet_status)
]

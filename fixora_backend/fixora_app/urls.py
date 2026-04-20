from django.urls import path
from . import views

urlpatterns = [
    path('service_list/', views.service_list, name='service_list'),
    path('new_service/', views.add_services, name='add_new_services'),
]

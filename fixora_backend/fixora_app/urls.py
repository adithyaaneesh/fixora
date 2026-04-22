from django.urls import path
from . import views

urlpatterns = [
    path('api/service_list/', views.service_list, name='service_list'),
    path('api/new_service/', views.add_services, name='add_new_services'),
    path('api/update_service/<int:pk>', views.update_service, name='update_service'),
    path('api/delete_service/<int:pk>', views.delete_service, name='delete_service'),
]

from django.urls import path
from .import views
# from .views import property_list

urlpatterns = [
    path('properties/', views.property_list, name = 'property_list' ),
    path('properties/<int:pk>/', views.property_detail, name= 'property_detail'),

    path('units/', views.unit_list, name = 'unit_list' ),
    path('units/<int:pk>/', views.unit_detail, name= 'unit_detail'),

    path('tenants/', views.tenant_list, name = 'tenant_list' ),
    path('tenants/<int:pk>/', views.tenant_detail, name= 'tenant_detail'),

    path('leases/', views.lease_list, name = 'lease_list' ),
    path('leases/<int:pk>/', views.lease_detail, name= 'lease_detail'),

]
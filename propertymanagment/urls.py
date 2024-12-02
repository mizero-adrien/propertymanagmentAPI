"""
URL configuration for propertymanagment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""


from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('propertyAPI/', include('property_app.urls')),

    path('propertyAPI/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('propertyAPI/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('propertyAPI/schema/redoc/', SpectacularRedocView.as_view(), name='redoc'),

    path('propertyAPI/token/', TokenObtainPairView.as_view(), name='token'),
    path('propertyAPI/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework import routers

from directory import views
from backend.views import *

# Auto Gens URLs
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('client/', views.client, name='client'),
    path('help/', views.help, name='help'),
    path('add_client', views.add_client, name='Add Client'),
    path('view_clients', views.view_clients, name='Client View'),

    # Adds URLS from router
    path('api/', include(router.urls)),

    # Generic endpoint? TBH IDK What it does
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

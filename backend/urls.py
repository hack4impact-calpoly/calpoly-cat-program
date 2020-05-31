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
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from directory import views
from backend.views import *

# Auto Gens API URLs
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cats', CatViewSet)
router.register(r'files', DocumentViewSet, basename='files')
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cat/', views.cat_profile, name='Cat Profile'),
    path('document_upload/', views.document_upload),
    path('delete_document/', views.delete_document),
    path('update_cat/', views.update_cat),
    path('intake/', views.intake_form, name='Intake Form'),
    path('help/', views.help, name='help'),

    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

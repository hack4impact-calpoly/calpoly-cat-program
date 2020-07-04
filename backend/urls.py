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
router.register(r'photos', PhotoViewSet, basename='photos')
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cat/', views.cat_profile, name='Cat Profile'),
    path('edit_profile/', views.update_cat),
    path('update_cat/', views.update_cat),
    path('intake/', views.intake_form, name='Intake Form'),

    path('document_upload/', views.document_upload),
    path('delete_document/', views.delete_document),
    path('photo_upload/', views.photo_upload),
    path('delete_photo/', views.delete_photo),

    path('events/', views.events, name='Events'),
    path('event/', views.single_event, name='Event'),
    path('delete_event/', views.delete_event),
    path('help/', views.help, name='help'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

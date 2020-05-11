from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions

from backend.serializers import *
from directory.models import Cat 

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint for adding and viewing Users/Admins/John
    """
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    # permission_classes = [permissions.IsAuthenticated]

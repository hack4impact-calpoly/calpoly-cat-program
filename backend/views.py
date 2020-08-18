from django.contrib.auth.models import User, Group
from django.db.models import OuterRef, Subquery

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from backend.serializers import *
from directory.models import Cat
from directory.models import Document
from directory.models import Event

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.filter(hidden=False)
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Cat.objects.filter(hidden=False)
        cat_id = self.request.query_params.get('cat_id', None)
        if cat_id is not None:
            queryset = queryset.filter(id=cat_id)
        return queryset

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Document.objects.filter(hidden=False)
        cat_id = self.request.query_params.get('cat_id', None)
        if cat_id is not None:
            queryset = queryset.filter(cat_id=cat_id)
        return queryset

class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Photo.objects.filter(hidden=False)
        cat_id = self.request.query_params.get('cat_id', None)
        if cat_id is not None:
            queryset = queryset.filter(cat_id=cat_id)
        return queryset

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        names = Cat.objects.filter(id=OuterRef('cat_id'))
        queryset = Event.objects.filter(hidden=False).annotate(name=Subquery(names.values('name')))

        if not self.request.user.is_superuser:
            queryset = queryset.exclude(event_type='vet')

        cat_id = self.request.query_params.get('cat_id', None)
        if cat_id is not None:
            queryset = queryset.filter(cat_id=cat_id)
        return queryset

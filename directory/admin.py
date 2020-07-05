from django.contrib import admin
from .models import Document, Photo, Event

# Register your models here.
admin.site.register(Document)
admin.site.register(Photo)
admin.site.register(Event)

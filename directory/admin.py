from django.contrib import admin
from .models import Cat, Document, Photo, Event

# Register your models here.
admin.site.register(Cat)
admin.site.register(Document)
admin.site.register(Photo)
admin.site.register(Event)

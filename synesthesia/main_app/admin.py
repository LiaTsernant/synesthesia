from django.contrib import admin
from .models import Note, Person, Picture
from django.contrib.auth.models import User


# Register all models for being able to see them as ADMIN
admin.site.register(Note)
admin.site.register(Person)
admin.site.register(Picture)


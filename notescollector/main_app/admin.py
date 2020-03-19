from django.contrib import admin
from .models import Note, Person, Picture

# Register your models here.
admin.site.register(Note)
admin.site.register(Person)
admin.site.register(Picture)


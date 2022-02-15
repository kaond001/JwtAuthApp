from django.contrib import admin

# Register your models here.
from .models import Note , Contact
admin.site.register(Note)
admin.site.register(Contact)
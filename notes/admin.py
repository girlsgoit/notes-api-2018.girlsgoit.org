from django.contrib import admin
from .models import NoteElement
from .models import Note

admin.site.register(NoteElement)
admin.site.register(Note)

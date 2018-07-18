from django.contrib import admin
from .models import NoteElement
from .models import Note
from .models import Comment

admin.site.register(NoteElement)
admin.site.register(Note)
admin.site.register(Comment)
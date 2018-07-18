from django.contrib import admin
from .models import NoteElement, Note, Comment, GGITUser

admin.site.register(GGITUser)
admin.site.register(NoteElement)
admin.site.register(Note)
admin.site.register(Comment)
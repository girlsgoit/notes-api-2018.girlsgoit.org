from django.urls import path
from .views import note_detail

urlpatterns = [
    path('notes/<int:note_id>', note_detail, name='note-detail')
]

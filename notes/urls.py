from django.urls import path
from .views import note_list
from .views import note_detail

urlpatterns = [
    path('notes/', note_list, name='note_list')
    path('notes/<int:note_id>', note_detail, name='note-detail')
]

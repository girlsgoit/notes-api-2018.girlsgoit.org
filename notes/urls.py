from django.urls import path
from .views import note_list

urlpatterns = [
    path('notes/', note_list, name='note_list')
]

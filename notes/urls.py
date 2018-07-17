from django.urls import path
from .views import note_list
from .views import note_detail, detail_view


urlpatterns = [
    path('notes/', note_list, name='note_list'),
    path('notes/<int:note_id>', note_detail, name='note-detail'),
    path('user/<int:user_id>', detail_view, name='user_details')
]

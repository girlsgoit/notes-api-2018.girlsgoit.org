from django.urls import path
from .views import note_list
from .views import note_detail
from .views import user_detail
from .views import note_detail
from .views import note_publish
from .views import user_unique 
from .views import note_done

urlpatterns = [
    path('notes/', note_list, name='note_list'),
    path('notes/<int:note_id>', note_detail, name='note-detail'),
    path('users/<int:user_id>', user_detail, name='user_details'),
    path('notes/<int:note_id>/publish/', note_publish, name='publish_note'),
    path('users/is-unique/', user_unique, name='user_unique'),
    path('notes/<int:note_id>/done/', note_done, name='note_done'),
]

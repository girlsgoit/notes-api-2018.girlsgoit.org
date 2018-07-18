from django.urls import path

from .views import (
    note_detail,
    note_done,
    note_list,
    note_publish,
    user_detail,
    user_unique
)

urlpatterns = [
    path('notes/', note_list, name='note_list'),
    path('notes/<int:note_id>', note_detail, name='note_detail'),
    path('notes/<int:note_id>/done/', note_done, name='note_done'),
    path('notes/<int:note_id>/publish/', note_publish, name='note_publish'),
    path('users/<int:user_id>', user_detail, name='user_detail'),
    path('users/is-unique/', user_unique, name='user_is_unique'),
]

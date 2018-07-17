from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET','PUT','DELETE'])
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'GET':
        note_serializer = NoteSerializer(note)
        return Response(note_serializer.data)

    elif request.method == 'PUT':
        new_note_data = request.data
        note_serializer = NoteSerializer(note, new_note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data)
        else:
            return Response(note_serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=200)
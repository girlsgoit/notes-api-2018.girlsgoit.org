from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

@api_view (['GET','POST'])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        note_serializer = NoteSerializer(notes, many=True)
        return Response(note_serializer.data)
    elif request.method == 'POST':
        note_data = request.data
        note_serializer = NoteSerializer (data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data)
        else:
            return Response(note_serializer.error, status=400)


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


@api_view(['POST'])
def note_publish(request, note_id):
    the_note = get_object_or_404(Note,pk=note_id) 

    if request.method == 'POST':
        the_note.published = True
        the_note.save()

        the_note_serializer = NoteSerializer(data=the_note_data)
        if the_note_serializer.is_valid():
            the_note_serializer.save()
            return Response(the_note_serializer.data, status=200)
        else:
            return Response(the_note_serializer.errors, status=400)

        
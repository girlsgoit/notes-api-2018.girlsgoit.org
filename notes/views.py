from django.shortcuts import render
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
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





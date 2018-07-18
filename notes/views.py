from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note, GGITUser
from .serializers import NoteSerializer, UserSerializer

@api_view (['GET', 'POST'])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        notes_serializer = NoteSerializer(notes, many=True)
        return Response(notes_serializer.data, status=200)

    elif request.method == 'POST':
        note_data = request.data
        note_data['user'] = request.user.id
        note_serializer = NoteSerializer(data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data, status=200)
        else:
            return Response(note_serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'GET':
        note_serializer = NoteSerializer(note)
        return Response(note_serializer.data, status=200)

    elif request.method == 'PUT':
        new_note_data = request.data
        new_note_data['user'] = request.user.id
        note_serializer = NoteSerializer(note, new_note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data, status=200)
        else:
            return Response(note_serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=200)


@api_view(['POST'])
def note_publish(request, note_id):
    note = get_object_or_404(Note,pk=note_id)

    if request.method == 'POST':
        note.published = True
        note.save()
        note_serializer = NoteSerializer(note)
        return Response(note_serializer.data, status=200)


@api_view (['POST'])
def note_done(request,note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        note.is_done = True
        note.save()
        note_serializer = NoteSerializer(note)
        return Response(note_serializer.data, status=200)


@api_view(['POST'])
def user_unique(request):
    users = GGITUser.objects.filter(username=request.data['username'])

    if request.method == 'POST':
        if users.exists():
            return Response(status=400)
        else:
            return Response(status=200)


@api_view(['GET', 'PUT'])
def user_detail(request, user_id):
    user = get_object_or_404(GGITUser, pk=user_id)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=200)

    elif request.method == 'PUT':
        user_new_data = request.data
        user_serializer = UserSerializer(user, user_new_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=200)
        else:
            return Response(user_serializer.error, status=400)


@api_view (['POST'])
def user_register(request):
    if request.method == 'POST':
        if request.data['password'] == request.data['confirm_password']:
            user = UserSerializer(data=request.data)
            if  user.is_valid():
                user.save()
                return Response(user.data,status=200)
            else:
                return Response(user.errors, status=400)
        else:
            return Response(status=400)

@api_view (['POST'])
def user_logout(request):
    if request.method == 'POST':
        print(request.user.id)

        
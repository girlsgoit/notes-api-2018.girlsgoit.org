from rest_framework import serializers
from .models import NoteElement
from .models import Note

class NoteElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteElement


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
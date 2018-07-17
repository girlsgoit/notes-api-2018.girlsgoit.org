from rest_framework import serializers
from .models import NoteElement

class NoteElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteElement
        fields = '__all__'
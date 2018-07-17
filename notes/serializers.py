from rest_framework import serializers
from .models import NoteElement, Note, Comment
from django.contrib.auth.models import User

class NoteElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteElement
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
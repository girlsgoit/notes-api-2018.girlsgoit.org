from rest_framework import serializers
from .models import NoteElement
from .models import Comment


class NoteElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteElement
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
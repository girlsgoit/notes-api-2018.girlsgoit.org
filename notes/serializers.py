from rest_framework import serializers
from .models import NoteElement, Note, Comment, GGITUser


class NoteElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteElement
        exclude = ['id', 'note']


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')

    class Meta:
        model = GGITUser
        fields = ['id', 'username', 'firstName', 'lastName', 'settings']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    note_elements = NoteElementSerializer(many=True)

    class Meta:
        model = Note
        fields = ['id', 'note_elements', 'created_date', 'modified_date', 'user', 'published', 'is_done']

    def create(self, validated_data):
        note_elements = validated_data['note_elements']
        note_obj = Note.objects.create(
            user=validated_data['user']
        )

        for note_element in note_elements:
            NoteElement.objects.create(
                tag=note_element['tag'],
                content=note_element['content'],
                note=note_obj
            )
        return note_obj

    def update(self, instance, validated_data):
        note_elements = validated_data['note_elements']
        instance.note_elements.all().delete()

        for note_element in note_elements:
            element = NoteElement.objects.create(
                tag=note_element['tag'],
                content=note_element['content'],
                note=instance
            )

        instance.save()
        return instance

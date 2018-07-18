from django.db import models
from django.contrib.auth.models import AbstractUser

class GGITUser(AbstractUser):
    settings = models.TextField()

    def __str__(self):
        return f"{self.username}"

class Note(models.Model):
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    user = models.ForeignKey(GGITUser, related_name='notes', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'Created date: {self.created_date}, modified date: {self.modified_date}, user: {self.user},{self.is_done}'


class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, related_name='note_elements', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag}, {self.note.id}'

class Comment(models.Model):
    author = models.ForeignKey(GGITUser, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}: {self.content}'



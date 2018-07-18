from django.db import models
from django.contrib.auth.models import AbstractUser


class GGITUser(AbstractUser):
    settings = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.username)


class Note(models.Model):
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    user = models.ForeignKey(GGITUser, related_name='notes', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return 'Created date: {}, User: {}'.format(self.created_date, self.user.username)

    def get_first_note_element(self):
        return self.note_elements.all()[:1]


class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, related_name='note_elements', on_delete=models.CASCADE)

    def __str__(self):
        return 'Tag: {}, Note: {}'.format(self.tag, self.note.id)


class Comment(models.Model):
    author = models.ForeignKey(GGITUser, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.author,  self.content)

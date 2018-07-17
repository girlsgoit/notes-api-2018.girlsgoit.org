from django.db import models

class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag}, {self.note.id}'
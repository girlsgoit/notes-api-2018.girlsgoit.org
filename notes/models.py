from django.db import models



class Note(models.Model):
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def __str__(self):
        return f'Created date: {self.created_date}, modified date: {self.modified_date}, user: {self.user}.'


class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, related_name='note_elements', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.tag}, {self.note.id}'

class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}: {self.content}'

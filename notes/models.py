from django.db import models

# Create your models here.

class Note(models.Model):
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def __str__(self):
        return f'Created date: {self.created_date}, modified date: {self.modified_date}, user: {self.user}.'

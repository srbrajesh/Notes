from django.db import models

# Create your models here.
class NewNote(models.Model):
    content = models.TextField()


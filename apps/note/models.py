from django.db import models

# Create your models here.

class Note(models.Model):
    author = models.CharField(max_length=60, null=False)
    title = models.CharField(max_length=60, null=True)
    note = models.CharField(max_length=500)
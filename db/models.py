from django.db import models

# Create your models here.

class Todo(models.Model):
    group = models.IntegerField()

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    due_date = models.DateField()
    
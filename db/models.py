from django.db import models

# Create your models here.

class Groups(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)

class Todo(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    due_date = models.DateField()
    
from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


def now():
    return datetime.now()


class ToDoItem(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=False, blank=False)
    completed = models.BooleanField(default=False)
    ts_created = models.DateTimeField(default=now)

    def __str__(self):
        return f"<task {self.author}>"

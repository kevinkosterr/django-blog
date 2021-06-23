from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


def now():
    return datetime.now()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    post_body = models.TextField()
    ts_posted = models.DateTimeField(default=now)
    ts_changed = models.DateTimeField(default=now)

    def __str__(self):
        return f'<{self.author}> {self.title} '

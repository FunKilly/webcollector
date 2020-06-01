import uuid

from django.db import models


class Website(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(max_length=200, default="")
    url = models.URLField(max_length=200, unique=True)
    text = models.TextField(max_length=100000, default="")
    raw_text = models.TextField(max_length=100000, default="")
    task_id = models.UUIDField(default=uuid.uuid4)

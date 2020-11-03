import uuid
from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    STATUS_CHOICE = [
        ('C', 'Created'), ('P', 'In progress'), ('D', 'Done')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000)
    status = models.CharField(choices=STATUS_CHOICE, default='C', max_length=100)
    user_id = models.ForeignKey(User, related_name='task', on_delete=models.SET_NULL, null=True)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    description = models.TextField()
    title = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_finished = models.BooleanField(default=False)
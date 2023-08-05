from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.ForeignKey(
        User,
        related_name="teacher",
        on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import User


class feedbackperson(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.email}'

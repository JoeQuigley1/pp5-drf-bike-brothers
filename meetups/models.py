from django.db import models
from django.contrib.auth.models import User


class MeetUps(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    city = models.CharField(max_length=50)
    venue = models.CharField(max_length=200)
    bike_type = models.CharField(max_length=50)
    spaces = models.IntegerField(blank=True)
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-date']


def __str__(self):
    return f'{self.id} {self.title}'

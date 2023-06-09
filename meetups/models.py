from django.db import models
from django.contrib.auth.models import User


class MeetUps(models.Model):
    """Model for a Meetup"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    city = models.CharField(max_length=50)
    venue = models.CharField(max_length=200)
    bike_type = models.CharField(max_length=50)
    spaces = models.IntegerField()
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-created_at']


def __str__(self):
    return f'{self.id} {self.title}'

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    bike_type_choices = [
        ('standard', 'Standard'),
        ('cruiser', 'Cruiser'),
        ('sports', 'Sports'),
        ('tourer', 'Tourer'),
        ('scrambler', 'Scrambler'),
        ('scooter', 'Scooter'),
        ('moped', 'Moped'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_wycmpt', blank=True
    )

    bike_type = models.CharField(
        max_length=50,
        choices=bike_type_choices,
        default='other',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

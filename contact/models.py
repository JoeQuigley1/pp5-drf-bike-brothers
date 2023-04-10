from django.db import models


class ContactForm(models.Model):
    """Model for a contact form """
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    email = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order by most recent first"""
        ordering = ['-created_on']

        def __str__(self):
            return f'{self.fname} {self.lname}'
from rest_framework import serializers
from contact.models import ContactForm


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactForm
        fields = [
            'fname',
            'lname',
            'email',
            'content',
            'created_at',

        ]

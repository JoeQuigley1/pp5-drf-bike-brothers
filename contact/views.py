from rest_framework import generics
from .models import ContactForm
from .serializers import ContactSerializer


class ContactDetail(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = ContactForm.objects.all()

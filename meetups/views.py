from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import MeetUps
from .serializers import MeetUpsSerializer

# Create your views here.

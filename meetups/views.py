from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import MeetUps
from .serializers import MeetUpsSerializer


class MeetUpsList(generics.ListCreateAPIView):

    serializer_class = MeetUpsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = MeetUps.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeetUpsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = MeetUpsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = queryset = MeetUps.objects.all()
from rest_framework import viewsets, permissions
from .serializers import MatchSerializer, ContributeSerializer
from .models import Match, Contribute

# Create your views here.


class MatchViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MatchSerializer
    queryset = Match.objects.all()


class ContributeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ContributeSerializer
    queryset = Contribute.objects.all()

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.permissions import IsAuthenticated

from .filters import SitesFilter
from .models import Sites
from .serializers import SitesSerializer


class SitesViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    list:
    Return Sites

    retrieve:
    Return Sites by id
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = SitesSerializer
    queryset = Sites.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SitesFilter

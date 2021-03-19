from django_filters import rest_framework as filters

from .models import Sites


class SitesFilter(filters.FilterSet):
    active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Sites
        fields = ['active']

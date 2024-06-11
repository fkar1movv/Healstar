from django_filters import rest_framework as filters

from core.models import Department, Hospital


class HospitalFilterSet(filters.FilterSet):
    ordering = filters.OrderingFilter(fields=['id', 'name'])
    address = filters.CharFilter(field_name='address', lookup_expr='icontains')
    country = filters.CharFilter(field_name='country', lookup_expr='icontains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Hospital
        fields = (
            'address',
            'country',
            'name',
        )


class DepartmentFilterSet(filters.FilterSet):
    ordering = filters.OrderingFilter(fields=['id', 'name'])
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Department
        fields = (
            'name',
        )

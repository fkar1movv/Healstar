from django_filters import rest_framework as filters

from users.models import Patient, Doctor


class PatientFilterSet(filters.FilterSet):
    name = filters.CharFilter(field_name='first_name', lookup_expr='icontains')

    class Meta:
        model = Patient
        fields = (
            'name',
        )


class DoctorFilterSet(filters.FilterSet):
    name = filters.CharFilter(field_name='first_name', lookup_expr='icontains')

    class Meta:
        model = Doctor
        fields = (
            'name',
        )

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Department, Hospital
from core.serializers import DepartmentSerializer, HospitalSerializer
from core.filters import DepartmentFilterSet, HospitalFilterSet


class DepartmentView(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DepartmentFilterSet


class HospitalView(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HospitalFilterSet

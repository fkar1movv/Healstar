from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend

from core import utils
from users import serializers
from users.models import Patient, Doctor
from users.filters import PatientFilterSet, DoctorFilterSet


class GenerateIDView(APIView):
    def post(self, request, *args, **kwargs):
        unique_id = utils.generate_unique_number()

        print('Request Data: ', request.data)

        cache.set(unique_id, request.data, timeout=60*6)  # patient info is stored for 6 minutes

        return Response(unique_id)


class CreatePatientView(APIView):

    def post(self, request, *args, **kwargs):
        patient_cred = request.data
        patient_id = kwargs.get('patient_id')

        # if patient_cred['password'] != patient_cred['password_confirm']:
        #     return Response(
        #         {'error': 'Passwords are not matching'},
        #         status=400
        #     )

        patient_info = cache.get(patient_id)
        if not patient_info:
            return Response(
                {'error': 'No patient info was found with given patient_id'},
                status=404
            )

        patient_info.update(
            {
                'email': patient_cred['email'],
                'password': patient_cred['password'],
                'patient_id': patient_id
            }
        )

        new_patient = Patient.objects.create(**patient_info)

        # Delete the patient info from cache
        cache.delete(patient_id)

        print('New Patient is created')

        return Response(
            {
                'id': new_patient.id,
                'patient_id': patient_id,
            },
            status=201
        )


class RetrievePatientView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer


class ListPatientView(GenericAPIView):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PatientFilterSet

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True).data

        return Response(serializer)


class CreateDoctorView(APIView):

    def post(self, request, *args, **kwargs):
        doctor_cred = request.data
        doctor_id = kwargs.get('doctor_id')

        if doctor_cred['password'] != doctor_cred['password_confirm']:
            return Response(
                {'error': 'Passwords are not matching'},
                status=400
            )

        doctor_info = cache.get(doctor_id)
        if not doctor_info:
            return Response(
                {'error': 'No doctor info was found with given doctor_id'},
                status=404
            )

        doctor_info.update(
            {
                'email': doctor_cred['email'],
                'password': doctor_cred['password'],
                'doctor_id': doctor_id
            }
        )

        new_doctor = Doctor.objects.create(**doctor_info)

        # Delete the patient info from cache
        cache.delete(doctor_id)

        return Response(
            {
                'id': new_doctor.id,
                'doctor_id': doctor_id,
            },
            status=201
        )


class RetrieveDoctorView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class ListDoctorView(GenericAPIView):
    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DoctorFilterSet

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True).data

        return Response(serializer)
